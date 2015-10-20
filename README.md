# altom-ro-tests

Small project running python webdriver tests against our website: 

http://altom.ro 

## CircleCI integration

This project uses cirlceci.com to automatically build and run tests after each commit. 

#### smoke-tests on master: <a href="https://circleci.com/gh/rucindrea/altom-ro-tests/tree/master" target="_blank"><img src="https://circleci.com/gh/rucindrea/altom-ro-tests/tree/master.png?circle-token=5254a837fff7f1b9926be1b0105b3788ff4ab37f ">
</a>
Check the circle.yml file for an example of how to run python tests in CircleCI

## Run locally

```
pip install selenium nose
cd altom-ro-tests
nosetests tests
```
