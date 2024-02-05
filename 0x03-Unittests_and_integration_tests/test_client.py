#!/usr/bin/env python3
"""This is a testing class"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """test class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json',
           return_value={"repos_url": "https://api.github.com/orgs/{org}"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        github_client = GithubOrgClient(org_name)
        response = github_client.org()
        self.assertEqual(response, {
            "repos_url": f"https://api.github.com/orgs/{org_name}"})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url returns the
        correct value"""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/test_org"}
        mock_org.return_value = test_payload

        github_client = GithubOrgClient("test_org")
        self.assertEqual(github_client._public_repos_url,
                         test_payload["repos_url"])

    @patch('client.get_json', return_value=[
        {"name": "repo1", "license": {"key": "my_license"}},
        {"name": "repo2"}])
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct
        value"""
        mock_public_repos_url.return_value = "https://api.github.com" \
                                             "/orgs/test_org"

        github_client = GithubOrgClient("test_org")
        self.assertEqual(github_client.public_repos(), ["repo1", "repo2"])
        self.assertEqual(github_client.public_repos("my_license"),
                         ["repo1"])

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test_org")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_output):
        """Test that GithubOrgClient.has_license returns the correct
        value"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected_output)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integeration test for module Fixtures"""

    @classmethod
    def setUpClass(cls):
        """Initially Run set up before the actual test"""
        config = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}

        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """clear the memory after a run"""
        cls.get_patcher.stop()

    def test_public_repo(self):
        """Integration test for the public_repo"""
        test_class = GithubOrgClient('Google')

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for the public repos with License"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()
