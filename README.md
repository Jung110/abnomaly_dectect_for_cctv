<details>
  <summary style = font-size :20pt>Table of Contents</summary>
  <ol>
    <li><a href="#overview">Overview</a></li>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#structure">Structure</a></li>
        </ul>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#reference">Reference</a></li>
  </ol>
</details>

<br>
<br>


# CCTV를 위한 이상행동 탐지

## Overview
---
### About
`‘자세 인식 딥러닝을 이용한 실시간 동영상 감시시스템 개발’` <br>
본 프로젝트는 동영상을 통해 `이상행동`을 인식하여 서버를 통해 알림을 주는 시스템을 구축하고자 했습니다.<br>
`주거단지 경비업체 혹은 공공 지자체` CCTV 모니터링 관리자를 보조하기 위해 만들어졌으며,
실내에 설치된 CCTV에서 영상을 받고 서버에서 행동을 분석하여 이상행동 발생시 알림이 웹페이지에 전달합니다.



### Structure

<br>

<image src = './img/about.png'>

<br>

## Built With
---
- <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

<br>

- <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/>

<br>

- <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>

<br>

- <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=PyTorch&logoColor=white"/>

## Getting started
---
- 파이썬 버젼 3.8.13으로 실행
```powershell
conda create -n test python=3.8.13 anaconda
activate test
```
- 장고 프로젝트에 필요한 requirement 설치

```powershell
pip install -r requirements.txt
# mysqlclient 미설치시 설치
pip install mysqlclient  
```
- mange.py를 이용하여 마이그레이션 및 실행 후 로컬 주소로 이동
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Usage
---
## License
---
MIT License를 따릅니다. LICENSE.md에서 자세한 정보를 알 수 있습니다. 
## Contact
---
 - Jung110 - aoemsltm119@gmail.com
 - Teo
 - alexturtleneckk
 - 
## Reference
---