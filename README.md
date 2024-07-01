# Fast Campus - 실전 장애 케이스 8가지 실습과 보고서 작성 

> [!CAUTION]
> 본 프로젝트의 시스템 구성에는 교육 목적을 위한 의도적인 결함이 존재합니다.
> This project presents a deliberately designed flawed system for educational purposes.

## 준비 사항

1. AWS 액세스 키와 시크릿 키를 발급받아 안전하게 보관하세요.
2. `secrets.tfvars` 라는 이름의 파일을 `infrastructure` 디렉토리 안에 생성하세요.
3. 해당 파일에 아래와 같이 채워 주세요.
    ```
    aws_access_key = "YOURAWSACCESSKEY"
    aws_secret_key = "YOURAWSSECRETACCESSKEY"
    ```
4. 터미널에서 `infrastructure` 디렉토리로 이동한 뒤 `terraform init`을 입력하세요.

## 테라폼 플래닝 및 인프라 적용

- 테라폼 코드를 플래닝하여 인프라가 어떻게 생성될지 보려면, `terraform plan -var-file=secrets.tfvars` 커맨드를 `infrastructure` 디렉토리에서 실행하세요.
- 실제로 테라폼 코드를 적용하여 인프라를 생성 또는 수정하고자 한다면, `terraform apply -var-file=secrets.tfvars` 커맨드를 `infrastructure` 디렉토리에서 실행하세요.
  - 약 20분 내외 소요됩니다.

## EKS 클러스터 접속

1. AWS CLI, `kubectl`, `helm`을 설치하세요.
2. `aws configure --profile fastcampus` 커맨드를 실행하여 AWS 액세스 키와 시크릿 키를 AWS CLI에서 사용하도록 설정하세요.
3. 터미널에서 `aws eks --region ap-northeast-2 update-kubeconfig --name fastcampus-infra-cluster --profile fastcampus`를 실행하여 `kubectl`을 통해 생성한 클러스터에 접근할 수 있도록 합니다.
4. 터미널에서 `kubectl config use-context arn:aws:eks:ap-northeast-2:1234567890:cluster/fastcampus-infra-cluster`을 실행해서 현재 쿠버네티스 컨텍스트를 생성한 클러스터를 바라보게 합니다. (`1234567890`을 본인의 계정 ID로 바꿔주세요.)
5. `kubectl get nodes` 커맨드를 실행해 노드 세 개가 정상적으로 출력되는지 확인해 주세요.

## 인프라 제거

1. 쿠버네티스 클러스터에 설치된 모든 자원을 제거하기 위해서, `helm uninstall fc-incident-scenarios` 커맨드를 입력해 주세요.
2. 프로비저닝된 모든 인프라를 제거하기 위해서, 터미널에서 `terraform destroy -var-file=secrets.tfvars` 커맨드를 입력해 주세요.
  - 약 10분 내외 소요됩니다.
3. 로컬 `kubectl` 설정 파일을 정리하기 위해서, 아래의 커맨드를 입력해 주세요.
  - `kubectl config delete-context arn:aws:eks:ap-northeast-2:1234567890:cluster/fastcampus-infra-cluster` (`1234567890`을 본인의 계정 ID로 바꿔주세요.)
  - `kubectl config delete-cluster arn:aws:eks:ap-northeast-2:1234567890:cluster/fastcampus-infra-cluster`
  - `kubectl config delete-user arn:aws:eks:ap-northeast-2:1234567890:cluster/fastcampus-infra-cluster`