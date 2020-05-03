class ZClass:

    @staticmethod
    def z(s: str) -> list:
        """
        Z-функция (англ. Z-function) от строки S и позиции x — это длина максимального префикса подстроки,
        начинающейся с позиции x в строке S, который одновременно является и префиксом всей строки S.
        :return:
        """
        out = []
        if not s:
            return out
        i, slen = 1, len(s)
        out.append(slen)
        while i < slen:
            left, right = 0, i
            while right < slen and s[left] == s[right]:
                left += 1
                right += 1
            out.append(left)
            i += 1
        return out

    @staticmethod
    def naive_z(s):
        n = len(s)
        z = [n]

        for i in range(1, n):
            left = right = i
            while right < n and s[right - left] == s[right]:
                right += 1
            z.append(right - left)
        return z

    def example(self):
        first = 'aacecaaa'
        print(first)
        print(self.z(first), '\n')

        second = 'abcdabcdabi'
        print(second)
        print(self.z(second), '\n')

        third = 'Все о том же поет луна. Все. Все о том же'
        print(third)
        print(self.z(third), '\n')

        forth = 'мне причем мне не очень'
        print(forth)
        print(self.z(forth), '\n')


z_class = ZClass()
z_class.example()
