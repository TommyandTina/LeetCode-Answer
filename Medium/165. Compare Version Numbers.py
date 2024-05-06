class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = [int(i) for i in version1.split('.')]
        version2_list = [int(i) for i in version2.split('.')]
        for i in range(max(len(version1_list), len(version2_list))):
            if i >= len(version1_list):
                version1_list.append(0)
            if i >= len(version2_list):
                version2_list.append(0)
            if version1_list[i] > version2_list[i]:
                return 1
            elif version1_list[i] < version2_list[i]:
                return -1
        return 0

#another version
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = [int(i) for i in version1.split('.')]
        version2_list = [int(i) for i in version2.split('.')]
        while len(version1_list) < len(version2_list):
            version1_list.append(0)
        while len(version2_list) < len(version1_list):
            version2_list.append(0)
        version1_int = int(''.join([str(i) for i in version1_list]))
        version2_int = int(''.join([str(i) for i in version2_list]))
        if version1_int > version2_int:
            return 1
        elif version1_int < version2_int:
            return -1
        return 0
