import pytest
import re
import sys


class TestAWS:

    def test_import(self):
        import vulcan.aws


class TestAWSSession:

    def test_import(self):
        from vulcan.aws import AWSSession


class TestAWSCloudFormation:

    def test_import(self):
        from vulcan.aws import AWSCloudFormation


class TestAWSCloudFront:

    def test_import(self):
        from vulcan.aws import AWSCloudFront


class TestAWSLambda:

    def test_import(self):
        from vulcan.aws import AWSLambda


class TestAWSS3:

    def test_import(self):
        from vulcan.aws import AWSS3


class TestAWSIAM:

    def test_import(self):
        from vulcan.aws import AWSIAM


class TestAWSEC2:

    def test_import(self):
        from vulcan.aws import AWSEC2
