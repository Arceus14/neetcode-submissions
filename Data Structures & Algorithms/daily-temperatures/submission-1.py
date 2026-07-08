class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # st = []
        # t_copy = temps.copy()
        # l = len(temps)
        # for i in range(l):
        #     t = temps[i]
        #     if st:
        #         top, itop = st[-1][0], st[-1][1]
        #         while top < t:
        #             temps[itop] = i - itop
        #             st.pop()
        #             if st:
        #                 top, itop = st[-1][0], st[-1][1]
        #             else:
        #                 break
        #         st.append((t, i))
        #     else:
        #         st.append((t, i))
        # for i in range(l):
        #     if temps[i] == t_copy[i]:
        #         temps[i] = 0
        # return temps   

        res = [0] * len(temps)
        st = []

        for i, t in enumerate(temps):
            while st and st[-1][0] < t:
                stTemp, stIndex = st.pop()
                res[stIndex] = i - stIndex
            st.append((t, i))   
        return res