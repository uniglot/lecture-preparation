resource "aws_db_instance" "rds" {
  identifier           = "${local.common_prefix}-db"
  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name
  vpc_security_group_ids = [ aws_db_subnet_group.rds_subnet_group.id ]

  engine         = "postgres"
  engine_version = local.rds_engine_version
  instance_class = local.rds_instance_class

  storage_type      = "gp3"
  allocated_storage = local.rds_allocated_storage

  db_name  = local.rds_db_name
  username = "fastcampus"
  password = var.rds_password
  port     = "5432"

  iam_database_authentication_enabled = true
  skip_final_snapshot                 = true
  deletion_protection                 = false
  publicly_accessible                 = false
}

resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "${local.common_prefix}-db-subnet-group"
  subnet_ids = module.vpc.private_subnets

  tags = {
    Name       = "${local.common_prefix}-db-subnet-group"
    Fastcampus = "true"
  }
}

resource "aws_security_group" "rds_security_group" {
  name   = "${local.common_prefix}-security-group"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [module.eks.cluster_security_group_id]
  }

  tags = {
    Name       = "${local.common_prefix}-security-group"
    Fastcampus = "true"
  }
}