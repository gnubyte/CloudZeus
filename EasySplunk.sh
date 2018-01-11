#! /bin/bash
# @Author: Patrick Hastings
# @AppVersion: 1.0.0
# @PythonVersion: 3.6.x
# @Title: SplunkEasyRootConsole
ACCESSKEY = ""
SECRETKEY = ""
REGION = ""
# ------------------------------
# Region listings here
echo "Easy Splunk setup - 1.0.0 "
printf "We are assuming you have python, \n and therego pip installed"
echo " This version of the software is intended for Splunk on AWS"
command -v pip3
if [ -z "$ACCESSKEY"]; then
    read -p "Enter AWS Access key ID:" ACCESSKEY
fi
pip install awscli
pip install boto3
echo " -------------"
echo "AWS Settings Entry"
echo "--------------"
echo "You will be prompted for your AWS IAM users Access ID and secret key"
echo "if you have not already created a IAM access key for your user, head to IAM and create one now"
echo "--------"
echo "You will be prompted for a region"
echo "For concanon training, enter: us-west-2"
aws configure