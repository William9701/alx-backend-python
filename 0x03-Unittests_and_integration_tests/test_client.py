#!/usr/bin/env python3
"""This is a testing class"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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

