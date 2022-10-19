
from dataclasses import dataclass, fields


class DriverApp(dict):
    def __init__(self,_main_page):
        _main_page = _main_page

    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)




_driver : DriverMaker
_driver._main_driver.page_source


class DriverElementXpath:
    element_path : str
    _driver : DriverMaker

    element = self._driver.find_element(By.XPATH,self.element_path)


class DriverCurrentElement:
    def __init__(self) -> None:
        pass
# _driver_.find_element(By.XPATH,adres_window_X) == DriverCurrentElement




filed_1 = DriverCurrentElement(current_driver)
filed_1.send_keys(adres)
filed_1.send_keys(Keys.RETURN)



filed_1[click,send_keys(adres_1),enter]
filed_1[click,send_keys(adres_2),enter]
filed_1[click,send_keys(adres),enter]
filed_1[click,send_keys(adres),enter]

Composite : DriverCurrentElement(current_driver)[click,send_keys(adres_1),enter]

cse:'click, send_keys, enter'
c : 'click'
DriverScope:
    _driver_main : driver
    composites_chain = List[Composite]



DriverScope(
    driver_name : 'search adress'
    _driver_main = driver,
    composites_chain(
        [[filed.perform('cse') for filed in fields]*10,
            filed_0['c']
        ])
            )

SiteLogic:
    Room : [DriverScope_1,DriverScope_2]


class InteractingDriverElement:

    enter = (r'\ue007')
    _click = _driver.find_element(By.XPATH,r'adres_2_window').click()
    _send_keys = _driver_.find_element(By.XPATH,adres_window_X).send_keys(adres)
    _enter = _driver_.find_element(By.XPATH,adres_window_X).send_keys(Keys.RETURN)

    ...

class IDElement(InteractingDriverElement): # BsInteracting()
    # find / finds : element
    info :
    text :
    ...


class IdeCombinations:
    def __init__(self,sequence_commands) -> None:

        self.sequence_commands = sequence_commands
    # [
    #     find_e , _send_keys, _enter
    # ]
    for ele in sequence_commands:
        curent_driver_elements.ele
