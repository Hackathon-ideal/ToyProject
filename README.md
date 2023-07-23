
## 🍕 프로젝트 소개 
랜덤으로 메뉴를 추천해 주는 웹 사이트입니다.
<br>

## 🍳 개발 기간 
* 2023년 7월 9일 ~ 2023년 7월 16일

### 🍙 멤버 구성
* FRONTEND
  * 김하경(PM): https://github.com/8lueis
  * 김도연: https://github.com/dotaeng
  * 허정윤: https://github.com/eksghgkssanta

* BACKEND
  * 박희선: https://github.com/heeseon1
  * 사은서: https://github.com/Saeunseo
  * 홍서윤: https://github.com/TjDbsws


### 🧀 개발 환경
* **Languages** : Python, HTML, CSS
* **Framework** : Django
* **IDE** : PyCharm, VSC
<br>


## 🍰 주요 기능
1. 모델 등록
```
class Korean(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='menu/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title
```

2. 카테고리 선택시 메뉴 랜덤 출력
```
def korean(request):
    koreanfoods = random.choice(Korean.objects.all())
    return render(request, 'photo/menu.html', {'koreanfoods': koreanfoods})
```
3. 템플릿 태그를 이용한 페이지 전환
```
<div class="LetSGo"
            <a href="{% url 'list' %}">LET’s GO!</a></div>
```
4. 추천 결과 페이지에 이미지, 텍스트 출력
```
#randomImage{
    width: 350px;
    left: 315px;
    position: absolute;
    top: 150px;
    z-index: 1;
}
```
```
 <img id="randomImage" src="{{koreanfoods.image.url}}" alt="{{koreanfoods.image}}" >
 <div class="menuText">{{koreanfoods.title}}</div>
```
                


<br>

## 🍪 시스템 동작
### 1. 메인 화면
<img width="800" alt="1" src="https://github.com/ToyProject-HW/ToyProject/assets/116551167/391bf9c0-5e8d-45c2-97c9-23afe8bec870">

### 2. 카테고리 선택 페이지
<img width="800" alt="2" src="https://github.com/ToyProject-HW/ToyProject/assets/116551167/0a0ebfe2-f0ce-431d-b4c7-93a5e06203a3">

### 3. 추천 결과 페이지
<img width="800" alt="3" src="https://github.com/ToyProject-HW/ToyProject/assets/116551167/99afb5da-b3fe-46b3-94c4-fc6eaae13526">
