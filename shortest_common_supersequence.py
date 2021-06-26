from typing import MutableMapping, Optional
from collections import defaultdict

# # Method 1 - Recursion: TLE
# class Solution:
#     def shortestCommonSupersequence(
#             self,
#             str1: str,
#             str2: str,
#             index1: int = 0,
#             index2: int = 0,
#     ) -> str:
#         if index1 >= len(str1):
#             return str2[index2:]
#
#         if index2 >= len(str2):
#             return str1[index1:]
#
#         char1 = str1[index1]
#         char2 = str2[index2]
#
#         if char1 == char2:
#             return char1 + self.shortestCommonSupersequence(str1, str2, index1+1, index2+1)
#
#         return min(
#             char1 + self.shortestCommonSupersequence(str1, str2, index1+1, index2),
#             char2 + self.shortestCommonSupersequence(str1, str2, index1, index2+1),
#             key=len
#         )


# # Method 2 - Memoization: TLE
# import sys
# sys.setrecursionlimit(10000)


# class Solution:
#     def shortestCommonSupersequence(
#             self,
#             str1: str,
#             str2: str,
#             index1: int = 0,
#             index2: int = 0,
#             cache: Optional[MutableMapping[int, MutableMapping[int, str]]] = None,
#     ) -> str:
#         if cache is None:
#             cache = defaultdict(lambda: defaultdict(str))
#
#         if index1 >= len(str1):
#             return str2[index2:]
#
#         if index2 >= len(str2):
#             return str1[index1:]
#
#         if index2 in cache[index1]:
#             return cache[index1][index2]
#
#         char1 = str1[index1]
#         char2 = str2[index2]
#
#         if char1 == char2:
#             result = char1 + self.shortestCommonSupersequence(str1, str2, index1+1, index2+1, cache)
#
#         else:
#             result = min(
#                 char1 + self.shortestCommonSupersequence(str1, str2, index1+1, index2, cache),
#                 char2 + self.shortestCommonSupersequence(str1, str2, index1, index2+1, cache),
#                 key=len
#             )
#
#         cache[index1][index2] = result
#         return result


# # Method 3 - Bottom-up DP: TLE
# class Solution:
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
#         cache: MutableMapping[int, MutableMapping[int, str]] = defaultdict(lambda: defaultdict(str))
#
#         # Initialization:
#         for index1 in range(1, len(str1)+1):
#             cache[index1][0] = str1[:index1]
#         for index2 in range(1, len(str2)+1):
#             cache[0][index2] = str2[:index2]
#
#         for index1, char1 in enumerate(str1, start=1):
#             for index2, char2 in enumerate(str2, start=1):
#                 if char1 == char2:
#                     cache[index1][index2] = cache[index1-1][index2-1] + char1
#                     continue
#
#                 cache[index1][index2] = min(
#                     cache[index1][index2-1] + char2,
#                     cache[index1-1][index2] + char1,
#                     key=len
#                 )
#
#         return cache[len(str1)][len(str2)]


# Method 4 - Bottom-up DP, optimized
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Instead of [index1], you use cache
        # Instead of [index1-1], you use prev_cache

        # First row initialization
        prev_cache: list[str] = [str2[:index2] for index2 in range(len(str2)+1)]

        for index1, char1 in enumerate(str1, start=1):
            cache = ['' for _ in range(len(str2)+1)]
            # First column initialization
            cache[0] = str1[:index1]

            for index2, char2 in enumerate(str2, start=1):
                if char1 == char2:
                    cache[index2] = prev_cache[index2-1] + char1
                    continue

                cache[index2] = min(
                    cache[index2-1] + char2,     # Instead of [index1][index2-1]
                    prev_cache[index2] + char1,  # Instead of [index1-1][index2]
                    key=len
                )

            # Don't forget to set the current row as previous row
            prev_cache = cache

        return cache[-1]


tests = [
    (
        ("abac", "cab",),
        "cabac",
    ),
    (
        ("akfwg", "fdawcgb",),
        "akfdawcgb",
    ),
    (
        ("atdznrqfwlfbcqkezrltzyeqvqemikzgghxkzenhtapwrmrovwtpzzsyiwongllqmvptwammerobtgmkpowndejvbuwbporfyroknrjoekdgqqlgzxiisweeegxajqlradgcciavbpgqjzwtdetmtallzyukdztoxysggrqkliixnagwzmassthjecvfzmyonglocmvjnxkcwqqvgrzpsswnigjthtkuawirecfuzrbifgwolpnhcapzxwmfhvpfmqapdxgmddsdlhteugqoyepbztspgojbrmpjmwmhnldunskpvwprzrudbmtwdvgyghgprqcdgqjjbyfsujnnssfqvjhnvcotynidziswpzhkdszbblustoxwtlhkowpatbypvkmajumsxqqunlxxvfezayrolwezfzfyzmmneepwshpemynwzyunsxgjflnqmfghsvwpknqhclhrlmnrljwabwpxomwhuhffpfinhnairblcayygghzqmotwrywqayvvgohmujneqlzurxcpnwdipldofyvfdurbsoxdurlofkqnrjomszjimrxbqzyazakkizojwkuzcacnbdifesoiesmkbyffcxhqgqyhwyubtsrqarqagogrnaxuzyggknksrfdrmnoxrctntngdxxechxrsbyhtlbmzgmcqopyixdomhnmvnsafphpkdgndcscbwyhueytaeodlhlzczmpqqmnilliydwtxtpedbncvsqauopbvygqdtcwehffagxmyoalogetacehnbfxlqhklvxfzmrjqofaesvuzfczeuqegwpcmahhpzodsmpvrvkzxxtsdsxwixiraphjlqawxinlwfspdlscdswtgjpoiixbvmpzilxrnpdvigpccnngxmlzoentslzyjjpkxemyiemoluhqifyonbnizcjrlmuylezdkkztcphlmwhnkdguhelqzjgvjtrzofmtpuhifoqnokonhqtzxmimp",
         "xjtuwbmvsdeogmnzorndhmjoqnqjnhmfueifqwleggctttilmfokpgotfykyzdhfafiervrsyuiseumzmymtvsdsowmovagekhevyqhifwevpepgmyhnagjtsciaecswebcuvxoavfgejqrxuvnhvkmolclecqsnsrjmxyokbkesaugbydfsupuqanetgunlqmundxvduqmzidatemaqmzzzfjpgmhyoktbdgpgbmjkhmfjtsxjqbfspedhzrxavhngtnuykpapwluameeqlutkyzyeffmqdsjyklmrxtioawcrvmsthbebdqqrpphncthosljfaeidboyekxezqtzlizqcvvxehrcskstshupglzgmbretpyehtavxegmbtznhpbczdjlzibnouxlxkeiedzoohoxhnhzqqaxdwetyudhyqvdhrggrszqeqkqqnunxqyyagyoptfkolieayokryidtctemtesuhbzczzvhlbbhnufjjocporuzuevofbuevuxhgexmckifntngaohfwqdakyobcooubdvypxjjxeugzdmapyamuwqtnqspsznyszhwqdqjxsmhdlkwkvlkdbjngvdmhvbllqqlcemkqxxdlldcfthjdqkyjrrjqqqpnmmelrwhtyugieuppqqtwychtpjmloxsckhzyitomjzypisxzztdwxhddvtvpleqdwamfnhhkszsfgfcdvakyqmmusdvihobdktesudmgmuaoovskvcapucntotdqxkrovzrtrrfvoczkfexwxujizcfiqflpbuuoyfuoovypstrtrxjuuecpjimbutnvqtiqvesaxrvzyxcwslttrgknbdcvvtkfqfzwudspeposxrfkkeqmdvlpazzjnywxjyaquirqpinaennweuobqvxnomuejansapnsrqivcateqngychblywxtdwntancarldwnloqyywrxrganyehkglbdeyshpodpmdchbcc",),
        "axjtuwbmvsdzeogmnzorndhmjoqnqjnhmfwlueifbcqkezrwltzyeqvqemggctttilmfokzgpghxotfykyzendhtfapwrmfierovwtpzzrsyuiwongllqseumvpzmymtvsdsowammerobtvagmekpowndhejvbuwbporfyroknrjoekdgqqlgzxihisfweevpepgxajqlrmyhnadgcjtsciavbpgqjzecswtdetmtallzybcukdztovxysgoavfgrejqkliirxuvnagwzmassthjecvfzkmyonglocmvjnxklecwqqvgrzpsswnigsrjthtmxyokuawirbkecfsauzrgbiydfsupuqanetgwounlpqmunhcapzdxwmfhvpfmduqmzidatemaqmzzzfjpdxgmddsdlhyokteubdgqoyepgbzmjkhmfjtspgoxjqbrmfspjmwmedhzrxavhnldugtnsuykpvwaprzrwludbameeqlutwdvgkyghgprqcdgqjjbzyefsujnnssfmqvjhnvcotynidziswpzhjykdszbblustomrxwtlhkiowpatbypwcrvkmajumsxthbebdqqurpphncthoslxxvjfezayreidbolwyekxezfqtzfylizmmneqcvvxepwhrcskstshpemynwzyunsxpgjflnqmfzgmbretpyehstavwpkxegmbtznqhpbclhrzdjlmzibnrouxljwabwpxkeiedzomwhuohffpfinoxhnairblcayygghzqmotwrywqayvvgohmujneqlzurxcpnwdiplwetyudofhyqvfduhrbsoxduggrlofszqeqkqqnrjomszjimrunxbqzyazyakgyoptfkolizeayojwkryidtctemtesuhbzcacnzzvhlbdibhnufjjocporuzuesvoifbuesvuxhgexmckbyfifcxhqntngqyaohfwyubtsrqarqdagkyogrnaxbcoouzbdvygpxjjxeugknksrfzdrmnoxrcapyamuwqtntqspszngdxxecyszhwqdqjxrsbymhtdlkwkvlkdbmzjngvdmhvbllqqlcemkqopyixxdomhnmvnsalldcfpthpkjdgqkyjrrjqqqpndcscbmmelrwyhtyugieyuppqqtaeodlwychtpjmlzoxsckhzyitomjzypqqmnilliysxzztdwtxhddvtvpleqdbwamfnhhkszsfgfcdvsqakyqmmusdvihopbvygqdktcwehffasudmgxmyoualogetovskvcapucehnbfxltotdqhklvxfzmkrjqofaesvuzrtrrfvoczeuqkfegxwpxujizcmahhfiqflpzbuuodsmpyfuoovypstrvkzxxtsdsxwixiraxjuuecphjlimbutnvqtiqvesawxinlrvzyxcwfspdlsttrgknbdcvvtkfqfzwudswtgjpepoiisxbvrfkkeqmdvlpazilzjnywxjyaquirnqpdvigpccnaengnweuobqvxmlznomuejantslzyjjapkxemynsrqivcatemoluhqifyonbnizgycjrhblmuylezwxtdkkzwntancpharlmdwhnkdguhelqzjgvjtrzofmtpuhifoqyywrxrganoyehkonglbdeyshqtzxmimpodpmdchbcc",
    ),

]
