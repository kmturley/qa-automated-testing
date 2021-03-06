# qa-automated-testing

Example project showing qa automated testing tools:

* [Behave](https://github.com/behave/behave) (End-to-End Tests)
* [Locust](https://github.com/locustio/locust) (Performance tests)
* [Selenium](https://github.com/baijum/selenium-python) (Functional Tests)
* [Zap](https://github.com/zaproxy/zap-api-python) (Penetration / Security Tests)


## Installation

First activate a virtual environment:

    pip install virtualenv
    virtualenv env
    source env/bin/activate

Then install the qa dependencies:

    pip install -r qa/requirements.txt


## Usage

Run the test server and selnium/zap services:

    docker-compose up

Run end-to-end tests using:

    behave qa/e2e/features

Run performance tests using:

    locust -f qa/performance/locustfile.py --clients 2 --hatch-rate 1 --num-request 4 --no-web --host=http://localhost:3000

Run penetration/security tests using:

    python qa/start_security.py
    behave qa/security/features


## Directory structure

    backend/                       --> Example server application
    qa/                            --> Automated qa tests


## Contact

For more information please contact kmturley
