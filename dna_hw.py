
class DNA(object):
    def __init__(self,string1, string2):
        self.string1= sqe1
        self.string2= sqe2

#     def count_nucleotides (self):
#         a=0
#         t=0
#         g=0
#         c=0
#         count=0
#         while count<= len(self.string1):
#             for i in self.string1:
#                 if i=='A' or i=='a':
#                     a+=1
#                 if i=='G' or i=='g':
#                     g+=1
#                 if i=='T' or i=='t':
#                     t+=1
#                     count+=1
#                     #это очень странно, но если не добавить каунт в любое условие, ответ увеличивается вдвое.Why? Окей это фиксится каунтом=1
#                 if i=='C' or i=='c':
#                     c+=1
#                 count+=1
#         d={'A:': a, 'G:': g, 'C:': c, 'T:': t}
#         return d
            
    # def transcribe(self):
    #     tseq=''
    #     count=1
    #     while count<=len(self.string1):
    #         for i in self.string1:
    #             if i=='t':
    #                 tseq += 'u'
    #             else: tseq+= i
    #             count+=1       
    #     return tseq
    
    # def complement_dna(self) -> str:
    #     compl=''
    #     for i in self.string1: 
    #         if i=='A' or i=='a':
    #             compl+= 't'
    #         if i=='G' or i=='g':
    #             compl+= 'c'
    #         if i=='T' or i=='t':
    #             compl+= 'a'
    #         if i=='C' or i=='c':
    #             compl+= 'G'
    #     complrev = compl[::-1]
    #     return complrev
    # def hamming_distance(self):
    #     def counter(m, n):
    #         if m != n:
    #             return 1
    #         return 0
    #     s = list(map(counter, self.string1, self.string2))
    #     return sum(s)


class RNA(object):
    def __init__(self, string):
        self.string= sqe3
    def transcribe(self):
        tseq=''
        count=1
        while count<=len(self.string):
            for i in self.string:
                if i=='u':
                    tseq += 't'
                else: tseq+= i
                count+=1
        return tseq
        
sqe1="ttt"
sqe2="t"
sqe3='uuugg'
rna=RNA(sqe3)
dna = DNA(sqe1, sqe2)
print(rna.transcribe())
