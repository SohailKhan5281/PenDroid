import os
import random
import socket
import time
import subprocess
import platform
import datetime
from datetime import datetime
from modules import banner
from modules import color
from modules import nmap


def start():
    # Creating Downloaded-Files folder if it does not exist
    try:
        # Creates a folder to store pulled files
        os.mkdir("Downloaded-Files")
    except:
        pass

    # Checking OS
    global operating_system, opener
    operating_system = platform.system()
    if operating_system == "Windows":
        # Windows specific configuration
        windows_config()
    else:
        # macOS only
        if operating_system == "Darwin":
            opener = "open"

        # On Linux and macOS both
        import readline  # Arrow Key

        check_packages()  # Checking for required packages


def windows_config():
    global clear, opener  # , move
    clear = "cls"
    opener = "start"
    # move = 'move'


def check_packages():
    adb_status = subprocess.call(["which", "adb"])
    scrcpy_status = subprocess.call(["which", "scrcpy"])
    metasploit_status = subprocess.call(["which", "msfconsole"])
    nmap_status = subprocess.call(["which", "nmap"])

    if (
        adb_status != 0
        or metasploit_status != 0
        or scrcpy_status != 0
        or nmap_status != 0
    ):
        print(
            f"\n{color.RED}ERROR : The following required software are NOT installed!\n"
        )

        count = 0  # Count variable for indexing

        if adb_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. {color.YELLOW}ADB{color.WHITE}")

        if metasploit_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. Metasploit-Framework{color.WHITE}")

        if scrcpy_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. Scrcpy{color.WHITE}")

        if nmap_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. Nmap{color.WHITE}")

        print(f"\n{color.CYAN}Please install the above listed software.{color.WHITE}\n")

        choice = input(
            f"\n{color.GREEN}Do you still want to continue to PhoneSploit Pro?{color.WHITE}     Y / N > "
        ).lower()
        if choice == "y" or choice == "":
            return
        elif choice == "n":
            exit_phonesploit_pro()
            return
        else:
            while choice != "y" and choice != "n" and choice != "":
                choice = input("\nInvalid choice!, Press Y or N > ").lower()
                if choice == "y" or choice == "":
                    return
                elif choice == "n":
                    exit_phonesploit_pro()
                    return

def userName():
        name = input("Enter your name: ").capitalize()
        id = generate_random_number()
        timeStamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        save_name_to_file(timeStamp,name, id)

def generate_random_number():
    return random.randint(1000, 10000)

def save_name_to_file(timeStamp, name, id):
    filename = 'UserLog.txt'

    with open(filename, 'a') as file:
        file.write(f"TimeStamp: {timeStamp}, Name: {name}, Id: {id}\n")

    print(f"Welcome {name} your unique is {id}.")

def display_menu():
    """Displays banner and menu"""
    print(selected_banner, page)


def clear_screen():
    """Clears the screen and display menu"""
    os.system(clear)
    display_menu()


def list_devices():
    print("\n")
    os.system("adb devices -l")
    print("\n")


def disconnect():
    print("\n")
    os.system("adb disconnect")
    print("\n")


def exit_phonesploit_pro():
    global run_phonesploit_pro
    run_phonesploit_pro = False
    print("\nExiting...\n")


def get_shell():
    print("\n")
    os.system("adb shell")


def get_screenshot():
    global screenshot_location
    # Getting a temporary file name to store time specific results
    instant = datetime.now()
    file_name = f"screenshot-{instant.year}-{instant.month}-{instant.day}-{instant.hour}-{instant.minute}-{instant.second}.png"
    os.system(f"adb shell screencap -p /sdcard/{file_name}")
    if screenshot_location == "":
        print(
            f"\n{color.YELLOW}Enter location to save all screenshots, Press 'Enter' for default{color.WHITE}"
        )
        screenshot_location = input("> ")
    if screenshot_location == "":
        screenshot_location = "Downloaded-Files"
        print(
            f"\n{color.PURPLE}Saving screenshot to PhoneSploit-Pro/{screenshot_location}\n{color.WHITE}"
        )
    else:
        print(
            f"\n{color.PURPLE}Saving screenshot to {screenshot_location}\n{color.WHITE}"
        )

    os.system(f"adb pull /sdcard/{file_name} {screenshot_location}")

    # Asking to open file
    choice = input(
        f"\n{color.GREEN}Do you want to Open the file?     Y / N {color.WHITE}> "
    ).lower()
    if choice == "y" or choice == "":
        os.system(f"{opener} {screenshot_location}/{file_name}")

    elif not choice == "n":
        while choice != "y" and choice != "n" and choice != "":
            choice = input("\nInvalid choice!, Press Y or N > ").lower()
            if choice == "y" or choice == "":
                os.system(f"{opener} {screenshot_location}/{file_name}")

    print("\n")


def screenrecord():
    global screenrecord_location
    # Getting a temporary file name to store time specific results
    instant = datetime.now()
    file_name = f"vid-{instant.year}-{instant.month}-{instant.day}-{instant.hour}-{instant.minute}-{instant.second}.mp4"

    duration = input(
        f"\n{color.CYAN}Enter the recording duration (in seconds) > {color.WHITE}"
    )
    print(f"\n{color.YELLOW}Starting Screen Recording...\n{color.WHITE}")
    os.system(
        f"adb shell screenrecord --verbose --time-limit {duration} /sdcard/{file_name}"
    )

    if screenrecord_location == "":
        print(
            f"\n{color.YELLOW}Enter location to save all videos, Press 'Enter' for default{color.WHITE}"
        )
        screenrecord_location = input("> ")
    if screenrecord_location == "":
        screenrecord_location = "Downloaded-Files"
        print(
            f"\n{color.PURPLE}Saving video to PhoneSploit-Pro/{screenrecord_location}\n{color.WHITE}"
        )
    else:
        print(f"\n{color.PURPLE}Saving video to {screenrecord_location}\n{color.WHITE}")

    os.system(f"adb pull /sdcard/{file_name} {screenrecord_location}")

    # Asking to open file
    choice = input(
        f"\n{color.GREEN}Do you want to Open the file?     Y / N {color.WHITE}> "
    ).lower()
    if choice == "y" or choice == "":
        os.system(f"{opener} {screenrecord_location}/{file_name}")

    elif not choice == "n":
        while choice != "y" and choice != "n" and choice != "":
            choice = input("\nInvalid choice!, Press Y or N > ").lower()
            if choice == "y" or choice == "":
                os.system(f"{opener} {screenrecord_location}/{file_name}")
    print("\n")


def uninstall_app():
    print(
        f"""
    {color.WHITE}1.{color.GREEN} Select from App List
    {color.WHITE}2.{color.GREEN} Enter Package Name Manually
    {color.WHITE}"""
    )

    mode = input("> ")
    if mode == "1":
        # Listing third party apps
        list = os.popen("adb shell pm list packages -3").read().split("\n")
        list.remove("")
        i = 0
        print("\n")
        for app in list:
            i += 1
            app = app.replace("package:", "")
            print(f"{color.GREEN}{i}.{color.WHITE} {app}")

        # Selection of app
        app = input("\nEnter Selection > ")
        if app.isdigit():
            if int(app) <= len(list) and int(app) > 0:
                package = list[int(app) - 1].replace("package:", "")
                print(f"\n{color.RED}Uninstalling {color.YELLOW}{package}{color.WHITE}")
                os.system("adb uninstall " + package)
            else:
                print(
                    f"\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}"
                )
                return
        else:
            print(
                f"\n{color.RED} Expected an Integer Value\n{color.GREEN} Going back to Main Menu{color.WHITE}"
            )
            return

    elif mode == "2":
        print(
            f"\n{color.CYAN}Enter package name     {color.WHITE}Example : com.spotify.music "
        )
        package_name = input("> ")

        if package_name == "":
            print(
                f"\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}"
            )
        else:
            os.system("adb uninstall " + package_name)
    else:
        print(
            f"\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}"
        )
        return

    print("\n")


def launch_app():
    print(
        f"""
    {color.WHITE}1.{color.GREEN} Select from App List
    {color.WHITE}2.{color.GREEN} Enter Package Name Manually
    {color.WHITE}"""
    )

    mode = input("> ")
    if mode == "1":
        # Listing third party apps
        list = os.popen("adb shell pm list packages -3").read().split("\n")
        list.remove("")
        i = 0
        print("\n")
        for app in list:
            i += 1
            app = app.replace("package:", "")
            print(f"{color.GREEN}{i}.{color.WHITE} {app}")

        # Selection of app
        app = input("\nEnter Selection > ")
        if app.isdigit():
            if int(app) <= len(list) and int(app) > 0:
                package_name = list[int(app) - 1].replace("package:", "")
            else:
                print(
                    f"\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}"
                )
                return
        else:
            print(
                f"\n{color.RED} Expected an Integer Value\n{color.GREEN} Going back to Main Menu{color.WHITE}"
            )
            return

    elif mode == "2":
        ## Old
        print(
            f"\n{color.CYAN}Enter package name :     {color.WHITE}Example : com.spotify.music "
        )
        package_name = input("> ")

        if package_name == "":
            print(
                f"\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}"
            )
            return

    os.system("adb shell monkey -p " + package_name + " 1")
    print("\n")


def list_apps():
    print(
        f"""

    {color.WHITE}1.{color.GREEN} List third party packages {color.WHITE}
    {color.WHITE}2.{color.GREEN} List all packages {color.WHITE}
    """
    )
    mode = input("> ")

    if mode == "1":
        list = os.popen("adb shell pm list packages -3").read().split("\n")
        list.remove("")
        i = 0
        print("\n")
        for app in list:
            i += 1
            app = app.replace("package:", "")
            print(f"{color.GREEN}{i}.{color.WHITE} {app}")
    elif mode == "2":
        list = os.popen("adb shell pm list packages").read().split("\n")
        list.remove("")
        i = 0
        print("\n")
        for app in list:
            i += 1
            app = app.replace("package:", "")
            print(f"{color.GREEN}{i}.{color.WHITE} {app}")
    else:
        print(
            f"\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}"
        )
    print("\n")


def reboot(key):
    print(
        f"\n{color.RED}[Warning]{color.YELLOW} Restarting will disconnect the device{color.WHITE}"
    )
    choice = input("\nDo you want to continue?     Y / N > ").lower()
    if choice == "y" or choice == "":
        pass
    elif choice == "n":
        return
    else:
        while choice != "y" and choice != "n" and choice != "":
            choice = input("\nInvalid choice!, Press Y or N > ").lower()
            if choice == "y" or choice == "":
                pass
            elif choice == "n":
                return

    if key == "system":
        os.system("adb reboot")
    else:
        print(
            f"""
    {color.WHITE}1.{color.GREEN} Reboot to Recovery Mode
    {color.WHITE}2.{color.GREEN} Reboot to Bootloader
    {color.WHITE}3.{color.GREEN} Reboot to Fastboot Mode
    {color.WHITE}"""
        )
        mode = input("> ")
        if mode == "1":
            os.system("adb reboot recovery")
        elif mode == "2":
            os.system("adb reboot bootloader")
        elif mode == "3":
            os.system("adb reboot fastboot")
        else:
            print(
                f"\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}"
            )
            return

    print("\n")


def list_files():
    print("\n")
    os.system("adb shell ls -a /sdcard/")
    print("\n")


def copy_whatsapp():
    global pull_location
    if pull_location == "":
        print(
            f"\n{color.YELLOW}Enter location to save WhatsApp Data, Press 'Enter' for default{color.WHITE}"
        )
        pull_location = input("> ")
    if pull_location == "":
        pull_location = "Downloaded-Files"
        print(
            f"\n{color.PURPLE}Saving data to PhoneSploit-Pro/{pull_location}\n{color.WHITE}"
        )
    else:
        print(f"\n{color.PURPLE}Saving data to {pull_location}\n{color.WHITE}")

    # folder_status = os.system(
    #     'adb shell test -d "/sdcard/Android/media/com.whatsapp/WhatsApp"')

    # 'test -d' checks if directory exist or not
    # If WhatsApp exists in Android
    if (
        os.system('adb shell test -d "/sdcard/Android/media/com.whatsapp/WhatsApp"')
        == 0
    ):
        location = "/sdcard/Android/media/com.whatsapp/WhatsApp"
    elif os.system('adb shell test -d "/sdcard/WhatsApp"') == 0:
        location = "/sdcard/WhatsApp"
    else:
        print(
            f"{color.RED}\n[Error]{color.GREEN} WhatsApp folder does not exist {color.GREEN}"
        )
        return

    os.system(f"adb pull {location} {pull_location}")
    print("\n")


def copy_screenshots():
    global pull_location
    if pull_location == "":
        print(
            f"\n{color.YELLOW}Enter location to save all Screenshots, Press 'Enter' for default{color.WHITE}"
        )
        pull_location = input("> ")

    if pull_location == "":
        pull_location = "Downloaded-Files"
        print(
            f"\n{color.PURPLE}Saving Screenshots to PhoneSploit-Pro/{pull_location}\n{color.WHITE}"
        )
    else:
        print(f"\n{color.PURPLE}Saving Screenshots to {pull_location}\n{color.WHITE}")

    # Checking if folder exists
    if os.system('adb shell test -d "/sdcard/Pictures/Screenshots"') == 0:
        location = "/sdcard/Pictures/Screenshots"
    elif os.system('adb shell test -d "/sdcard/DCIM/Screenshots"') == 0:
        location = "/sdcard/DCIM/Screenshots"
    elif os.system('adb shell test -d "/sdcard/Screenshots"') == 0:
        location = "/sdcard/Screenshots"
    else:
        print(
            f"{color.RED}\n[Error]{color.GREEN} Screenshots folder does not exist {color.GREEN}"
        )
        return
    os.system(f"adb pull {location} {pull_location}")
    print("\n")


def copy_camera():
    global pull_location
    if pull_location == "":
        print(
            f"\n{color.YELLOW}Enter location to save all Photos, Press 'Enter' for default{color.WHITE}"
        )
        pull_location = input("> ")
    if pull_location == "":
        pull_location = "Downloaded-Files"
        print(
            f"\n{color.PURPLE}Saving Photos to PhoneSploit-Pro/{pull_location}\n{color.WHITE}"
        )
    else:
        print(f"\n{color.PURPLE}Saving Photos to {pull_location}\n{color.WHITE}")

    # Checking if folder exists
    if os.system('adb shell test -d "/sdcard/DCIM/Camera"') == 0:
        location = "/sdcard/DCIM/Camera"
    else:
        print(
            f"{color.RED}\n[Error]{color.GREEN} Camera folder does not exist {color.GREEN}"
        )
        return
    os.system(f"adb pull {location} {pull_location}")
    print("\n")


def open_link():
    print(
        f"\n{color.YELLOW}Enter URL              {color.CYAN}Example : https://web.radav.org/ {color.WHITE}"
    )
    url = input("> ")

    if url == "":
        print(
            f"\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}"
        )
        return
    else:
        print(f'\n{color.YELLOW}Opening "{url}" on device        \n{color.WHITE}')
        os.system(f"adb shell am start -a android.intent.action.VIEW -d {url}")
        print("\n")


def open_photo():
    location = input(
        f"\n{color.YELLOW}Enter Photo location in computer{color.WHITE} > "
    )

    if location == "":
        print(
            f"\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}"
        )
        return
    else:
        if location[len(location) - 1] == " ":
            location = location.removesuffix(" ")
        location = location.replace("'", "")
        location = location.replace('"', "")
        if not os.path.isfile(location):
            print(
                f"{color.RED}\n[Error]{color.GREEN} This file does not exist {color.GREEN}"
            )
            return
        else:
            location = '"' + location + '"'
            os.system("adb push " + location + " /sdcard/")

        file_path = location.split("/")
        file_name = file_path[len(file_path) - 1]

        # Reverse slash ('\') splitting for Windows only
        global operating_system
        if operating_system == "Windows":
            file_path = file_name.split("\\")
            file_name = file_path[len(file_path) - 1]

        file_name = file_name.replace("'", "")
        file_name = file_name.replace('"', "")
        file_name = "'" + file_name + "'"
        print(file_name)
        print(f"\n{color.YELLOW}Opening Photo on device        \n{color.WHITE}")
        os.system(
            f'adb shell am start -a android.intent.action.VIEW -d "file:///sdcard/{file_name}" -t image/jpeg'
        )  # -n com.android.chrome/com.google.android.apps.chrome.Main
        print("\n")


def open_video():
    location = input(
        f"\n{color.YELLOW}Enter Video location in computer{color.WHITE} > "
    )

    if location == "":
        print(
            f"\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}"
        )
        return
    else:
        if location[len(location) - 1] == " ":
            location = location.removesuffix(" ")
        location = location.replace("'", "")
        location = location.replace('"', "")
        if not os.path.isfile(location):
            print(
                f"{color.RED}\n[Error]{color.GREEN} This file does not exist {color.GREEN}"
            )
            return
        else:
            location = '"' + location + '"'
            os.system("adb push " + location + " /sdcard/")

        file_path = location.split("/")
        file_name = file_path[len(file_path) - 1]

        # Reverse slash ('\') splitting for Windows only
        global operating_system
        if operating_system == "Windows":
            file_path = file_name.split("\\")
            file_name = file_path[len(file_path) - 1]

        file_name = file_name.replace("'", "")
        file_name = file_name.replace('"', "")
        file_name = "'" + file_name + "'"
        print(file_name)

        print(f"\n{color.YELLOW}Playing Video on device        \n{color.WHITE}")
        os.system(
            f'adb shell am start -a android.intent.action.VIEW -d "file:///sdcard/{file_name}" -t video/mp4'
        )
        print("\n")


def get_device_info():
    model = os.popen(f"adb shell getprop ro.product.model").read()
    manufacturer = os.popen(f"adb shell getprop ro.product.manufacturer").read()
    chipset = os.popen(f"adb shell getprop ro.product.board").read()
    android = os.popen(f"adb shell getprop ro.build.version.release").read()
    security_patch = os.popen(
        f"adb shell getprop ro.build.version.security_patch"
    ).read()
    device = os.popen(f"adb shell getprop ro.product.vendor.device").read()
    sim = os.popen(f"adb shell getprop gsm.sim.operator.alpha").read()
    encryption_state = os.popen(f"adb shell getprop ro.crypto.state").read()
    build_date = os.popen(f"adb shell getprop ro.build.date").read()
    sdk_version = os.popen(f"adb shell getprop ro.build.version.sdk").read()
    wifi_interface = os.popen(f"adb shell getprop wifi.interface").read()

    print(
        f"""
    {color.YELLOW}Model :{color.WHITE} {model}\
    {color.YELLOW}Manufacturer :{color.WHITE} {manufacturer}\
    {color.YELLOW}Chipset :{color.WHITE} {chipset}\
    {color.YELLOW}Android Version :{color.WHITE} {android}\
    {color.YELLOW}Security Patch :{color.WHITE} {security_patch}\
    {color.YELLOW}Device :{color.WHITE} {device}\
    {color.YELLOW}SIM :{color.WHITE} {sim}\
    {color.YELLOW}Encryption State :{color.WHITE} {encryption_state}\
    {color.YELLOW}Build Date :{color.WHITE} {build_date}\
    {color.YELLOW}SDK Version :{color.WHITE} {sdk_version}\
    {color.YELLOW}WiFi Interface :{color.WHITE} {wifi_interface}\
"""
    )


def battery_info():
    battery = os.popen(f"adb shell dumpsys battery").read()
    print(
        f"""\n{color.YELLOW}Battery Information :
{color.WHITE}{battery}\n"""
    )


def unlock_device():
    password = input(
        f"{color.YELLOW}\nEnter password or Press 'Enter' for blank{color.WHITE} > "
    )
    os.system("adb shell input keyevent 26")
    os.system("adb shell input swipe 200 900 200 300 200")
    if not password == "":  # if password is not blank
        os.system(f'adb shell input text "{password}"')
    os.system("adb shell input keyevent 66")
    print(f"{color.GREEN}\nDevice unlocked{color.WHITE}")


def lock_device():
    os.system("adb shell input keyevent 26")
    print(f"{color.GREEN}\nDevice locked{color.WHITE}")


def mirror():
    print(
        f"""
    {color.WHITE}1.{color.GREEN} Default Mode   {color.YELLOW}(Best quality)
    {color.WHITE}2.{color.GREEN} Fast Mode      {color.YELLOW}(Low quality but high performance)
    {color.WHITE}3.{color.GREEN} Custom Mode    {color.YELLOW}(Tweak settings to increase performance)
    {color.WHITE}"""
    )
    mode = input("> ")
    if mode == "1":
        os.system("scrcpy")
    elif mode == "2":
        os.system("scrcpy -m 1024 -b 1M")
    elif mode == "3":
        print(f"\n{color.CYAN}Enter size limit {color.YELLOW}(e.g. 1024){color.WHITE}")
        size = input("> ")
        if not size == "":
            size = "-m " + size

        print(
            f"\n{color.CYAN}Enter bit-rate {color.YELLOW}(e.g. 2)   {color.WHITE}(Default : 8 Mbps)"
        )
        bitrate = input("> ")
        if not bitrate == "":
            bitrate = "-b " + bitrate + "M"

        print(f"\n{color.CYAN}Enter frame-rate {color.YELLOW}(e.g. 15){color.WHITE}")
        framerate = input("> ")
        if not framerate == "":
            framerate = "--max-fps=" + framerate

        os.system(f"scrcpy {size} {bitrate} {framerate}")
    else:
        print(
            f"\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}"
        )
        return
    print("\n")


def power_off():
    print(
        f"\n{color.RED}[Warning]{color.YELLOW} Powering off device will disconnect the device{color.WHITE}"
    )
    choice = input("\nDo you want to continue?     Y / N > ").lower()
    if choice == "y" or choice == "":
        pass
    elif choice == "n":
        return
    else:
        while choice != "y" and choice != "n" and choice != "":
            choice = input("\nInvalid choice!, Press Y or N > ").lower()
            if choice == "y" or choice == "":
                pass
            elif choice == "n":
                return
    os.system(f"adb shell reboot -p")
    print("\n")

def stop_adb():
    os.system("adb kill-server")
    print("\nStopped ADB Server")

def create_report(users):
    with open("Report.txt", "a") as log_file:
        for user in users:
            timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S")
            log_data = f"\nTimestamp: {timestamp}\nName: {user['name']}\nID: {user['id']}\nDescription: {user['description']}\n------------------------------------------"
            log_file.write(log_data)

def report():
    num_users = int(input("Welcome! Please enter the number of users:"))

    users = []
    
    for _ in range(num_users):
        name = input("Name: ").capitalize()
        while name=="":
            print("Please enter your name:")
            name = input("Name: ").capitalize()
        user_id = input("ID: ")
        while user_id=="" or user_id.isalpha():
            print("Please a valid id:")
            user_id = input("ID: ")
        description = input("Description: ")
        while description=="":
            print("Description is mandatory:")
            description = input("Description: ")

        user_data = {'name': name, 'id': user_id, 'description': description}
        users.append(user_data)

    create_report(users)

    print("Log file created successfully!")

def main():
    print(f"\n {color.WHITE}cls: Clear Screen                e: Exit")
    option = input(f"\n{color.RED}[Main Menu] {color.WHITE}Enter selection > ").lower()

    match option:
        case "release":
            from modules import release
        case "e":
            exit_phonesploit_pro()
        case "cls":
            clear_screen()
        case "1":
            userName()
        case "2":
            list_devices()
        case "3":
            disconnect()
        case "4":
            mirror()
        case "5":
            get_screenshot()
        case "6":
            screenrecord()
        case "7":
            launch_app()
        case "8":
            open_link()
        case "9":
            open_photo()
        case "21":
            open_video()
        case "12":
            get_device_info()
        case "13":
            battery_info()
        case "14":
            reboot("system")
        case "15":
            reboot("advanced")
        case "16":
            lock_device()
        case "22":
            uninstall_app()
        case "23":
            list_apps()
        case "18":
            list_files()
        case "19":
            copy_whatsapp()
        case "20":
            copy_screenshots()
        case "17":
            copy_camera()
        case "11":
            stop_adb()
        case "10":
            power_off()
        case "24":
            report()
        case other:
            print("\nInvalid selection!\n")


# Global variables
run_phonesploit_pro = True
operating_system = ""
clear = "clear"
opener = "xdg-open"
# move = 'mv'
page_number = 0
page = banner.menu[page_number]

# Locations
screenshot_location = ""
screenrecord_location = ""
pull_location = ""

# Concatenating banner color with the selected banner
selected_banner = random.choice(color.color_list) + random.choice(banner.banner_list)

start()

if run_phonesploit_pro:
    clear_screen()
    while run_phonesploit_pro:
        try:
            main()
        except KeyboardInterrupt:
            exit_phonesploit_pro()
