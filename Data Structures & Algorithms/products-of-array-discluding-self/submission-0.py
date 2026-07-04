class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        suffix_product = []
        output = []

        base = 1
        for num in nums:
            base  = base * num
            prefix_product.append(base) 

        base = 1
        for num in nums[::-1]:
            base  = base * num
            suffix_product.append(base)

        suffix_product = suffix_product[::-1]
        suffix_product.append(1)

        for i in range(len(nums)):
            product_except_self = prefix_product[i] * suffix_product[i+1]
            output.append(product_except_self)

        return output




        