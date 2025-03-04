# HTML?

### Hyper Text Markup Language

> Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
>
> Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

### HTML이란?

> 웹 페이지를 작성(구조화)하기 위한 언어

## HTML 기본구조

> **html** : 문서의 최상위(root) 요소
>
> **head** : 문서 메타데이터 요소
>
> * 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
> * 일반적으로 브라우저에 나타나지 않는 내용
>
> **body** : 문서 본문 요소
>
> * 실제 화면 구성과 관련된 내용

### 요소(element)

![image-20220801194631138](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220801194631138.png)

> **시작 태그 / 내용 / 종료 태그**
>
> * 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미 정의
>
>   내용이 없을 수 도 있음 : br, hr, img, input, link, meta  등
>
> * 요소는 중첩(nested)될 수 있음
>   * 요소의 중첩을 통해 하나의 문서 구조화
>   * 여는 태그와 닫는 태그 쌍을 잘 확인하지 않으면 오류 반환이 아닌 레이아웃이 깨진 상태로 출력 돼 디버깅이 힘듬

### 속성(attribute)

![image-20220801194907422](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220801194907422.png)

> 속성을 통해 태그의 부가적인 정보 설정 가능
>
> 요소는 속성을 가질 수 있음
>
> 요소의 시작 태그에 작성, 보통 이름 값이 하나의 쌍으로 존재

### HTML Global Attribute : 태그와 상관없이 사용 가능한 속성

> **id** : 문서 전체에서 유일한 고유 식별자 지정
>
> **class** : 공백으로 구분된 해당 요소의 클래스의 목록
>
> **data-\*** : 페이지에 개인 사용자 정의 데이터를 저장
>
> **style** :  inline 스타일
>
> **title** : 요소에 대한 추가 정보 지정
>
> **tabindex** : 요소의 탭 순서

### 시맨틱 태그

> HTML 태그가 특정 목적, 역할 및 의미적 가치(semantic value)를 가지는 것
>
> Non semantic 요소 : div, span

**대표적인 시맨틱 태그 목록**

> **header** : 문서 전체나 섹션의 헤더(머리말 부분)
>
> **nav** : 내비게이션
>
> **aside** : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
>
> **section** : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
>
> **article** : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
>
> **footer** : 문서 전체나 섹션의 푸터(마지막 부분)

### 시맨틱 태그 사용 이유

**의미론적 마크업**

> 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
>
> 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
>
> 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수 쉽게함
>
> 검색 엔진 최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함

### 렌더링(Rendinrg)

> 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

### DOM(Document Object Model)트리

> 테그스트 파일인 HTML 문서를 브라우조에서 렌더링 하기 위한 구조

![image-20220801195925461](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220801195925461.png)



