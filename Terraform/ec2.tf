resource "aws_instance" "nuevo_ec2" {
  ami             = "ami-0e83be366243f524a"
  instance_type   = "t2.micro"
  key_name        = "llaves2"
  security_groups = [aws_security_group.sG_new.id]
  subnet_id = "subnet-0d956ef522bfc25c5"

  tags = {
    Name = "nuevo_ec2"
  }
}

output "My_ip"{
  value = aws_instance.nuevo_ec2.public_ip
}


resource "aws_security_group" "sG_new" {
  name        = "HTTP"
  description = "Permite HTTP Y SSH"
  vpc_id      = "vpc-034cc79748fd2a532"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

   ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}

