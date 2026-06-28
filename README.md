<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>




<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Python Authenication Tool</h1>

  <p align="center">
    This app provides a signle sign on solutions for the .
    <br />
    <a href='https://github.com/azimmerman17/python-authenticator'><strong>Explore the docs »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# About The Project

This project (Python Authenication Tool) was buit to provide a single sign in solution across all the applications I plan to build and maintain.  This authenicator, provides a means of basic token exchange to create, authenticate a user,  persist their login, and reset a password. 

This application also provides the application with basic profile information, to allow data consistancy accross multiple appilcations, without requireing users to update the information oon each application.

 It was not the intention of this application to provide high end security and it would not be recommended to use this tool for applications that may use sensistive information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Built With
[![python][python]][python-url] 
[![flask][flask]][flask-url] 
[![mySQL][mySQL]][mySQL-url] 
[![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url] 
[![JWT][JWT]][JWT-url] 
[![Postman][Postman]][Postman-url]
<!-- [![Vercel][Vercel]][Vercel-url] -->


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
# Getting Started


## Installation

1. Clone the repo
  ```sh
  git clone https://github.com/azimmerman17/python-authenticator.git
  ```

2. Create virtual environment
  ```sh
  python3 -m venv .venv
  ```

3. Activate the virtual environment
  ```sh
  . .venv/bin/activate
  ```

4. Install Python packages 
  ```sh
  pip install requirements.txt
  ```

5. Configure your .env file

  ```sh
  ENV='Enter the current enviroment'
  PORT='Enter the your desired port'
  MYSQL_DATABASE='Name of your MySQL database'
  MYSQL_PASSWORD='Password for your MySQL database'
  MYSQL_PORT='MySQL database port'
  MYSQL_HOST='MySQL databace host'
  MYSQL_URI= 'Enter your mySQL database connection string'
  ENCRYPTION_KEY='Enter your encryption key'
  PEPPER='Enter a random string'
  ALGORITHM='Enter your encrypting algorith'
  IV_LENGTH='Enter the desired IV Length'
  JWT_SECRET='Enter you JSON-Web-Token secert'
  JWT_ACCESS_TOKEN_EXPIRES = 'Enter number of hours the JWT will be valid'
  SECRET_KEY='Enter a secert key to authenticate incoming requests'
  MAIL_SERVER='Enter your Email STMP host'
  MAIL_PORT='Enter your desired Email port'
  MAIL_USERNAME='Enter your Email username'
  MAIL_PASSWORD='Enter your email password or Dual factor authentication code'
  MAIL_REPLY = 'Enter a reply-to email address, if different from your sending email'
  ```

 - PORT is optional. I use PORT to designate which port I use with local development
 - ENV is used with emails routed.  If this value is set to 'PROD' emails will sent set to the user.  All other values will send email to the address set in MAIL_USERNAME

6. Mirgate the DataBase Table - Utilizing Flask-Mirgrate

  [Flask-Migrate Documentation][Flask-Migrate-url]

  ```sh
  flask db init
  flask db upgrade
  ```


6. start your server
  ```sh
  flask run --debug --port {PORT}
  ```

  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
# Usage

## Tables

#### Users

Table to store a user's indentity 

| Column | Type | Allow Null | Unique | Default Value | Description |
| --- | --- | --- | --- | --- |  --- |
| person_id | Serial | False | True | N/A | Generated id number for the user |
| user_name | String | False | True | N/A | Username created by the user |
| first_name | String | True | False | N/A | Person's first name |
| last_name | String | True | False | N/A | Person's last name |
| email | String | False | True | N/A | Person's email |
| salt | String | False | False | N/A | Generated Salt Value for Password Hashing |
| password_hash | String | False | False | N/A | Person's hased password |
| reset_token | String | True | False | N/A | Token to validate a reset password request |
| reset_expire | Date | True | False | N/A |  Timestamp to the guid token to xpire |
| created_at | Date | False | False | NOW() | Timestamp of record's creation |
| updated_at | Date | False | False | NOW() | Timestamp of record's last update |

### EndPoints

API documentation to come


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Connect to active or developing app and apply bug fixes
- [ ] Deploy hosted envirnment
- [ ] Build Role table 

See the [open issues](https://github.com/azimmerman17/python-authenticator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Andrew Zimmerman - azimmerman@pga.com

Project Link: [https://github.com/azimmerman17/python-authenticator](https://github.com/azimmerman17/python-authenticator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments



<p align="right">(<a href="#readme-top">back to top</a>)</p>

 -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- BADGES -->
[contributors-shield]: https://img.shields.io/github/contributors/azimmerman17/python-authenticator.svg?style=for-the-badge
[contributors-url]: https://github.com/azimmerman17/python-authenticator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/azimmerman17/python-authenticator.svg?style=for-the-badge
[forks-url]: https://github.com/azimmerman17/python-authenticator/network/members
[stars-shield]: https://img.shields.io/github/stars/azimmerman17/python-authenticator.svg?style=for-the-badge
[stars-url]: https://github.com/azimmerman17/python-authenticator/stargazers
[issues-shield]: https://img.shields.io/github/issues/azimmerman17/python-authenticator.svg?style=for-the-badge
[issues-url]: https://github.com/azimmerman17/python-authenticator/issues
[license-shield]: https://img.shields.io/github/license/azimmerman17/python-authenticator.svg?style=for-the-badge
[license-url]: https://github.com/azimmerman17/python-authenticator/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077b5?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0nMjU2JyBoZWlnaHQ9JzI1NicgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSd4TWlkWU1pZCcgdmlld0JveD0nMCAwIDI1NiAyNTYnPjxwYXRoIGQ9J00yMTguMTIzIDIxOC4xMjdoLTM3LjkzMXYtNTkuNDAzYzAtMTQuMTY1LS4yNTMtMzIuNC0xOS43MjgtMzIuNC0xOS43NTYgMC0yMi43NzkgMTUuNDM0LTIyLjc3OSAzMS4zNjl2NjAuNDNoLTM3LjkzVjk1Ljk2N2gzNi40MTN2MTYuNjk0aC41MWEzOS45MDcgMzkuOTA3IDAgMCAxIDM1LjkyOC0xOS43MzNjMzguNDQ1IDAgNDUuNTMzIDI1LjI4OCA0NS41MzMgNTguMTg2bC0uMDE2IDY3LjAxM1pNNTYuOTU1IDc5LjI3Yy0xMi4xNTcuMDAyLTIyLjAxNC05Ljg1Mi0yMi4wMTYtMjIuMDA5LS4wMDItMTIuMTU3IDkuODUxLTIyLjAxNCAyMi4wMDgtMjIuMDE2IDEyLjE1Ny0uMDAzIDIyLjAxNCA5Ljg1MSAyMi4wMTYgMjIuMDA4QTIyLjAxMyAyMi4wMTMgMCAwIDEgNTYuOTU1IDc5LjI3bTE4Ljk2NiAxMzguODU4SDM3Ljk1Vjk1Ljk2N2gzNy45N3YxMjIuMTZaTTIzNy4wMzMuMDE4SDE4Ljg5QzguNTgtLjA5OC4xMjUgOC4xNjEtLjAwMSAxOC40NzF2MjE5LjA1M2MuMTIyIDEwLjMxNSA4LjU3NiAxOC41ODIgMTguODkgMTguNDc0aDIxOC4xNDRjMTAuMzM2LjEyOCAxOC44MjMtOC4xMzkgMTguOTY2LTE4LjQ3NFYxOC40NTRjLS4xNDctMTAuMzMtOC42MzUtMTguNTg4LTE4Ljk2Ni0xOC40NTMnIGZpbGw9JyNmZmYnLz48L3N2Zz4K
[linkedin-url]: https://linkedin.com/in/azimmerman17

<!-- PACKAGES -->
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org
[flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/
[mySQL]: https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[mySQL-url]: https://www.mysql.com
[SQLAlchemy]: https://img.shields.io/badge/-SQLAlchemy-323330?style=for-the-badge&logo=sqlalchemy&logoColor=CE563D
[SQLAlchemy-url]: https://www.sqlalchemy.org
[JWT]: https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens
[JWT-url]: https://www.jwt.io
[Postman]:https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white
[Postman-url]: https://www.postman.com/
[Flask-Migrate-url]: https://flask-migrate.readthedocs.io/en/latest/
[Vercel]: https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white
[Vercel-url]: https://vercel.com/

