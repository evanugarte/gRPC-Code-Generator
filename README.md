# gRPC-Code-Generator
Using Amazon EC2, Amazon S3, Flask and gRPC, this tool aims to abstract the
 generation of code from gRPC `.proto` files.

## Project Architecture
This project has code split across a client and a server.
![Project Architecture](https://user-images.githubusercontent.com/36345325/88504599-11d79900-cf8a-11ea-87f4-459b2e8d4d1a.png)

### Client Code
This will run locally on a user's machine and accept a proto file as well as 
languages to generate code for. The code for the client can be found in
 [`proto-gen-cli.py`](https://github.com/evanugarte/gRPC-Code-Generator/blob/master/proto-gen-cli.py)

### Server Code
The server accepts code generation requests from the client and uploads
 generated code to an S3 bucket. To learn more about the server's workflow
 check out the section of the video [here](https://youtu.be/WRIzwziBDQI?t=977).
 All code for the server can be found in
 [`ec2`](https://github.com/evanugarte/gRPC-Code-Generator/blob/master/ec2).

## Are you here from the [video](https://www.youtube.com/watch?v=WRIzwziBDQI)?
Here are the snippets to copy:
### `ProtoFileGenerator`'s Code Generation Functions:
```py
def generate_node_files(self):
    os.system(f'protoc-gen-grpc \
              --js_out=import_style=commonjs,binary:./ \
              --grpc_out=./ --proto_path ./ \
              ./{self.proto_file.filename}')

def generate_python_files(self):
    os.system(f'python3 -m grpc_tools.protoc -I. --python_out=./ \
              --grpc_python_out=./ {self.proto_file.filename}')
```

### S3 Bucket Policy:
```json
{
    "Version": "2012-10-17",
    "Id": "Policyxxxx961",
    "Statement": [
        {
            "Sid": "Stmtxxxxx4365",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::<BUCKET NAME HERE>",
                "arn:aws:s3:::<BUCKET NAME HERE>/*"
            ]
        },
        {
            "Sid": "Stmt1488493308547",
            "Effect": "Allow",
            "Principal": {
                "AWS": "<AWS IAM USER ARN HERE>"
            },
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:GetBucketLocation",
                "s3:Get*",
                "s3:Put*"
            ],
            "Resource": "arn:aws:s3:::<BUCKET NAME HERE>"
        }
    ]
}
```
**Note:** You need to replace `<BUCKET NAME HERE>` with your s3 bucket name.

**Note 2:** You'll also need to replace `<AWS IAM USER ARN HERE>` with your IAM
 user's ARN (looks like `arn:aws:iam::xxxxxxxxxx:user/username`).

### S3 CORS Policy:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

### Docker Container Setup Script:
You can find it in [`ec2/setup`](https://github.com/evanugarte/gRPC-Code-Generator/blob/master/ec2/setup)

### `Dockerfile` for EC2 Instance:
Check out [`ec2/Dockerfile`](https://github.com/evanugarte/gRPC-Code-Generator/blob/master/ec2/Dockerfile)
