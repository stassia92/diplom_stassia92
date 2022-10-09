from selenium.webdriver.common.by import By

header_web = (By.CSS_SELECTOR, '#content > h1')
header_examples = (By.CSS_SELECTOR, '#content > h2')
main_page_footer = (By.CSS_SELECTOR, '#page-footer > div > div')
github_btn = (By.CSS_SELECTOR, 'body > div:nth-child(2) > a > img')
github_name = (By.CSS_SELECTOR, '#repository-container-header > '
                                'div.d-flex.flex-wrap.flex-justify-end.mb-3.px-3.px-md-4.px-lg-5 >'
                                ' div > div > '
                                'span.author.flex-self-stretch > a')
github_btn_image = (By.TAG_NAME, 'img')
add_and_remove = (By.LINK_TEXT, 'Add/Remove Elements')
add_element_btn = (By.CSS_SELECTOR, "#content > div > button")
del_element_btn = (By.CSS_SELECTOR, "#elements > button")
elements = (By.CSS_SELECTOR, "#elements")
auth_log_in_txt = (By.CSS_SELECTOR, "#content > div > p")
checkboxes = (By.LINK_TEXT, 'Checkboxes')
checkbox_2 = (By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")
checkbox_1 = (By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
dropdown_example = (By.LINK_TEXT, 'Dropdown')
dropdown = (By.ID, "dropdown")
option_1_txt_on_page = (By.XPATH, "//*[contains(text(),'Option 1')]")
option_2_txt_on_page = (By.XPATH, "//*[contains(text(),'Option 2')]")
context_menu = (By.LINK_TEXT, 'Context Menu')
right_click_spot = (By.CSS_SELECTOR, "#hot-spot")
form_authentication = (By.LINK_TEXT, 'Form Authentication')
username = (By.ID, 'username')
password = (By.ID, 'password')
login_btn = (By.CSS_SELECTOR, '#login > button')
login_success = (By.ID, "flash-messages")
file_upload = (By.CSS_SELECTOR, '#content > ul > li:nth-child(18) > a')
choose_file = (By.XPATH, '//*[@id="file-upload"]')
upload_btn = (By.CSS_SELECTOR, '#file-submit')
upload_success_txt = (By.CSS_SELECTOR, '#content > div > h3')
error_if_file_not_uploaded = (By.CSS_SELECTOR, 'body > h1')
dynamic_controls = (By.LINK_TEXT, 'Dynamic Controls')
checkbox_dinamic = (By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
remove_and_add_btn = (By.CSS_SELECTOR, '#checkbox-example > button')
message = (By.ID, "message")
enable_disable_btn = (By.CSS_SELECTOR, '#input-example > button')
hovers_page = (By.LINK_TEXT, 'Hovers')
hover_1 = (By.CSS_SELECTOR, '#content > div > div:nth-child(3) > img')
hidden_user1_txt = (By.CSS_SELECTOR, '#content > div > div:nth-child(3) > div > h5')
hover_2 = (By.CSS_SELECTOR, '#content > div > div:nth-child(4) > img')
hidden_user2_txt = (By.CSS_SELECTOR, '#content > div > div:nth-child(4) > div > h5')
hover_3 = (By.CSS_SELECTOR, '#content > div > div:nth-child(5) > img')
hidden_user3_txt = (By.CSS_SELECTOR, '#content > div > div:nth-child(5) > div > h5')
status_code_examples = (By.LINK_TEXT, 'Status Codes')
code_200 = (By.CSS_SELECTOR, '#content > div > ul > li:nth-child(1) > a')
code_301 = (By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > a')
code_404 = (By.CSS_SELECTOR, '#content > div > ul > li:nth-child(3) > a')
code_500 = (By.CSS_SELECTOR, '#content > div > ul > li:nth-child(4) > a')
frames_example = (By.LINK_TEXT, 'Frames')
iframe = (By.LINK_TEXT, 'iFrame')
iframe_txt = (By.ID, 'tinymce')
nested_frame_example = (By.LINK_TEXT, 'Nested Frames')
frame_bottom = (By.NAME, 'frame-bottom')
frames_body = (By.XPATH, "//body")
text_frame = (By.CSS_SELECTOR, '#tinymce > p')

