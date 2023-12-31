
# AC

API test 

## Installation

Install [api-test-assignment](https://github.com/saikiranshet/api-test-assignment) with pipenv

```bash
pipenv install
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_ID`

`API_TOKEN`

`BASE_URL`


## Execute

To execute the test suite

```bash
pytest -vs --html=reports/report.html
```
To execute the test using markers

```bash
pytest -vsm "smoke" --html=reports/report.html
pytest -vsm "regression" --html=reports/report.html
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

