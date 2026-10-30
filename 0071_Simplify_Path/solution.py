class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        rec_path = path.split("/")
        print(rec_path)


        res = []
        for s in rec_path:
            if s=="" or s==".":
                continue
            if s == "..":
                if len(res)>0:
                    res.pop()

            else:
                res.append(s)


        out = "/"
        if len(res)==0:
            return out

        for p in res:
            out = out+p+"/"

        out = out[:-1]

        return out




                