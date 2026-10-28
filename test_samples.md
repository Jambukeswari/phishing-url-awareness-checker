
# Test Samples

## Test 1
URL: https://www.example.com/login
Expected result: No listed warning signs found. This does NOT prove safety.

## Test 2
URL: http://192.0.2.10/account
Expected result: IP address warning and HTTP warning.

## Test 3
URL: http://example.com@sample.invalid/login
Expected result: @ symbol warning and HTTP warning.

## Test 4
URL: https://a.b.c.d.e.example.invalid/path
Expected result: Many hostname segments warning.

## Test 5
URL: https://xn--example.invalid/
Expected result: Punycode-style hostname warning.