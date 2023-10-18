# 🇹🇷 터키아제르바이잔어과 50주년 기념 사이트 🇦🇿
## 🌟 소개

<img width="400" alt="image" src="https://github.com/leehjhjhj/tuaz50th/assets/102458609/889f3529-a394-41ca-aeb4-ea2a87957a9b">
<img width="400" alt="image" src="https://github.com/leehjhjhj/tuaz50th/assets/102458609/aa88b94b-d0c7-4013-b533-7d887da12c03">
<img width="400" alt="image" src="https://github.com/leehjhjhj/tuaz50th/assets/102458609/4f96fa6d-442a-47ae-b962-6c2fdc02edf6">
<img width="400" alt="image" src="https://github.com/leehjhjhj/tuaz50th/assets/102458609/e7f57433-a2b2-40d7-98f6-55df6fb2e600">
<img width="400" alt="image" src="https://github.com/leehjhjhj/tuaz50th/assets/102458609/f909d184-ba87-42b3-ad13-f038b503e773">
<img width="400" alt="image" src="https://github.com/leehjhjhj/tuaz50th/assets/102458609/f11ca87a-201a-498b-b015-dc97bd9da9ac">

https://tuaz50th.kro.kr
- 터키아제르바이잔어과 50주년 행사를 기념하여 만들어진 터키어과 굿즈 사이트입니다.
- 상품 주문, 주문 조회, 주문 취소, 어드민 페이지 커스텀
  
## 🛠️ 기술 스택
- Django, Aws S3, Github actions

## ☺️ 회고
### 또 한번의 비개발자와의 협업
개발지식이 없는 비개발자인 과학생회와 학생회장와 프로젝트를 진행하게 된 값진 경험이었습니다. 기능적인 요구가 있었을 때, 무조건 안된다는 마인드보다 최대한 열린 귀로 수용하고 타협점을 찾아 나갔습니다. 학생회와의 꾸준한 회의와 소통으로 필요한 기능만 빠르게 개발할 수 있었습니다. 상품 주문, 주문 조회, 주문 취소가 핵심 기능이며 실제 이 사이트를 통해서 상품을 구매하는 과구성원들의 편의성을 위해서 회원가입을 하지 않는 방향으로 개발하였습니다. 디자이너를 비롯한 프론트엔드 개발자 또한 존재하지 않았기 때문에 초반에 난항이 있었지만, 지속적인 피드백을 비롯한 상호 존중으로 기능 추가를 거듭해 나가면서 개발을 완료했습니다.

### 관리자의 관점을 생각하다.
구매를 하는 과구성원의 관점은 물론, 주문 관리를 하는 학생회의 관점도 생각해보는 경험을 하였습니다. 주문 정보가 주문 상품에 따라서, 주문 상태에 따라서 산재되어 있으면 관리가 힘들다고 판단하였습니다. 그래서 Django의 Admin을 주문 상태에 따른 필터링을 비롯한 주문과 주문 아이템을 한눈에 볼 수 있게 기능을 커스텀하여서 관리자가 보다 쉽게 주문을 관리할 수 있도록 노력했습니다. 주문 기간이 완료된 이후에, 제작 업체에 제공할 주문 정보 테이블을 만들기 위해서 실제 DB의 데이터를 가공하기 위해 직접 쿼리문을 작성하는 경험을 하였습니다. 
쿼리문 참고: https://imasimdi.tistory.com/178
