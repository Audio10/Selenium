# Selenium

## Test elements

To start to read a test we needs to have two methods, the **setUp** and **tearDown**. This methods allows to setUp the environment for the tests. What happens before and after.

### Example

```
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver = self.driver
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://demo.onestepcheckout.com/')
  

  def tearDown(self):
        self.driver.quit()
```

## Elements selection

The examples are in **HomePageTests**

## Test suites

Compilation of tests in a single test, this allows to have group or individual results.

## Implicit wait and explicit wait

**Implicit wait**: This going to find one or more elements in the DOM until the time expired.

**Explicit wait**: This use a conditional to wait a element until the conditional is true.

