# Parallel  [![Created by kim jinho][kim-jinho-badge-image]]

<b>Parallel<b>은 페어 트레이딩을 위한 웹 프레임워크입니다.

관리자 아이디는 vipasset, 패스워드는 vipasset9973입니다.

현재 버전은 배포용이 아니므로 사용이 불가능합니다.

Framework Structure
-------------

>앱 구성은 Sauron, Delorean, Insights로 되어 있습니다.
>
>Sauron : Pair Scanner
>
>Delorean : Backtester  

    parallel
    ├── ...
    ├── core                    # 메인 페이지
    │   ├── benchmarks          # Load and stress tests
    │   ├── integration         # End-to-end, integration tests (alternatively `e2e`)
    │   └── unit                # Unit tests
    ├── delorean                # 백테스터
    ├── portfolio               # 기본 파일
    │   ├── settings          # Load and stress tests
    │   ├── urls         # End-to-end, integration tests (alternatively `e2e`)
    │   └── wsgi                # Unit tests
    ├── parallel                # 메인 폴더
    ├── db.sqlite3              # DB
    ├── README.md               # 설명서
    └── manage.py               # 



License
-------

parallel is Copyright © 2019- Kim Jinho.



[community]: https://thoughtbot.com/community?utm_source=github

[kim-jinho-badge-image]: https://img.shields.io/badge/Created_by-kim_jinho-8E64B0.svg