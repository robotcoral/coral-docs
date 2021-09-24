import sys
import requests


def throw_error(text):
    print("❌ ERROR: " + text)
    sys.exit(1)


def throw_warning(text):
    print("⚠️ WARNING: " + text)


def get_version():
    respone = requests.get(
        "https://api.github.com/repos/robotcoral/coral-app/releases/latest"
    ).json()
    return respone["tag_name"]


def new_version_greater(new_ver, old_ver):
    new_ver = list(map(int, new_ver.split(".")))
    old_ver = list(map(int, old_ver.split(".")))
    for i in range(0, 3):
        if new_ver[i] > old_ver[i]:
            return True

    return False


def bump_documentation(version):
    print("\n> Loading conf.py")
    with open("./source/conf.py", "r") as f:
        file = f.read()

    begin_version_line = file.find('release = "')
    begin_version = begin_version_line + len('release = "')
    end_version = file.find('"', begin_version)
    env_com_version = file[begin_version:end_version]

    print("Old Version: " + env_com_version)
    print("New Version: " + version)

    check_version = new_version_greater(version, env_com_version)

    if not (check_version):
        throw_warning("New version is <= old version")

        print("✅ SUCCESS - no changes")
        return

    print("> Writing to conf.py")
    with open("./source/conf.py", "w") as f:
        f.write(file[0:begin_version] + version + file[end_version:])

    print("✅ SUCCESS")


def export_version(version):
    with open("./doc_version.txt", "w") as f:
        f.write(version)


def bump_version(version):
    bump_documentation(version)


if __name__ == "__main__":
    print("### Robot Coral CI ###\n")

    print("---Loading new version number---")

    version = get_version()

    print("\n---Bumping versions---")

    print("New version: " + version)
    bump_version(version)
    export_version(version)

    print("\n----------")
    print("\n✅ SUCCESS")
