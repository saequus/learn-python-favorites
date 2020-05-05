import math


class JumpSearch:

    @staticmethod
    def find(arr, target):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0

        while arr[int(min(n, step) - 1)] < target:
            prev = step
            step += step
            if step > n:
                return -1

            if arr[int(prev)] == target:
                return prev
        while arr[int(prev)] < target:
            prev += 1
            if prev == min(step, n):
                return -1

            if arr[int(prev)] == target:
                return prev
        return -1


test_arr = [1, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target_element_value = 55


def main():
    jump = JumpSearch()
    print('\n   Find target element with value %s in array: ' % target_element_value)
    print('  ', ' '.join(str(_) for _ in test_arr))
    print('   using jump find algorithm \n')
    print('   Target element index position: ', jump.find(test_arr, target_element_value), '\n')


if __name__ == '__main__':
    main()
