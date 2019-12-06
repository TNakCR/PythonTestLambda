# PythonTestLambda

pip3 install boto3 -t ./

pip3 install pymysql -t ./

pip3 install pandas -t ./

pip3 install sqlalchemy -t ./

chmod -R 755 .

zip -r ../myDeploymentPackage.zip .


====================

aws --profile ansibleaws-c4-dev  lambda create-function --function-name test-lambda --code S3Bucket=chromeriver-lambdarepo-c4-dev,S3Key=lambda.zip  --role "arn:aws:iam::196666950711:role/prosper-c4-dev"  --environment Variables="{JDBC_URL='jdbc:mysql://c4-dev-navigatordb-0.cemtanyak0jn.us-west-2.rds.amazonaws.com:3306' , PASSWORD='testpassword'  , USERNAME='cr_tester'}" --runtime python3.7 --handler lambda_function.lambda_handler --description "Hello World" --memory-size 256 --timeout 60  --vpc-config SubnetIds="subnet-00a0b18cd80d0076e,subnet-01d44b5c8a5d4f936,subnet-0ef11717dde506808",SecurityGroupIds="sg-01306e94c71806dc9"

======================

aws --profile ansibleaws-c4-dev lambda invoke  --function-name arn:aws:lambda:us-west-2:196666950711:function:test-lambda --invocation-type RequestResponse outfile.txt

=======================

aws --profile ansibleaws-c4-dev  lambda  delete-function --function-name test-lambda

=================

aws --profile ansibleaws-c4-dev --region us-west-2 s3 sync /tmp/upload/ s3://chromeriver-lambdarepo-c4-dev


====================

https://pypi.org/project/pandas/#files

https://pypi.org/project/s3fs/#files

numpy-1.17.4-cp37-cp37m-manylinux1_x86_64.whl
unzip numpy-1.17.4-cp37-cp37m-manylinux1_x86_64.whl
pandas-0.25.3-cp37-cp37m-manylinux1_x86_64.whl
unzip pandas-0.25.3-cp37-cp37m-manylinux1_x86_64.whl
s3fs-0.4.0-py3-none-any.whl
unzip s3fs-0.4.0-py3-none-any.whl
