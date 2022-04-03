from molgrafik import *
class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedQ:
    def __init__(self, first = None, last= None):
        self.__first = first
        self.__last = last

    def enqueue(self, value):
        #Köar värden och länkar samman den nya Node med tidigare Node samt ändrar last pointern
        if(self.isEmpty()):
            self.__first = Node(value)
        else:
            if(self.__first.next == None):
                self.__last = Node(value)
                self.__first.next = self.__last
            else:
                self.__last.next = Node(value)
                self.__last = self.__last.next
        return

    def dequeue(self):
        #Tar ut första Node ur kön och ändrar first pointern
        if(not self.isEmpty()):
            temp_value = self.__first.value
            self.__first = self.__first.next
            return temp_value
        else:
            return

    def isEmpty(self):
        #Kollar om första objektet är tomt och därav om länkade listan är tom
        if(self.__first == None):
            return True
        else:
            return False

    def size(self):
        #returnerar storleken av den länkade listan
        counter = 0
        temp_node = self.__first
        while temp_node.next != None:
            temp_node = temp_node.next
            counter += 1
        return counter

    def peek(self):
        if (self.__first != None):
            return self.__first.value
        return None
atomer = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
higher = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
nr = ["0","1","2","3","4","5","6","7","8","9"]
error = ""
rutanFirst = None

class Atom:
    #Taget från hashtest.py i laboration 7: Hashtabeller
    def __init__(self, namn, vikt):
        self.namn = namn
        self.vikt = vikt
    def __str__(self):
        return "{" + self.namn + " " +  str(self.vikt) + "}"
    def getnamn(self):
        return self.namn
    def getvikt(self):
        return self.vikt

def skapaAtomlista():
    #Taget från hashtest.py i laboration 7: Hashtabeller
    """Skapar och returnerar en lista med Atom-objekt"""
    atomdata = "H  1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B  10.811;\
    C  12.0107;\
    N  14.0067;\
    O  15.9994;\
    F  18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P  30.973762;\
    S  32.065;\
    Cl 35.453;\
    K  39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V  50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y  88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I  126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W  183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U  238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"
    atomlista = []
    lista = atomdata.split(";")
    for namn_vikt in lista:
        namn, vikt = namn_vikt.split()
        atom = Atom(namn, float(vikt))
        atomlista.append(atom)
    return atomlista

class molekylException(Exception):
    pass

def weight(mol, atomLista):
    #atom.getvikt()
    vikt = 0
    if(not mol.atom =="( )"):
        for i in range(len(atomLista)):
            if(atomLista[i].getnamn() == mol.atom):
                vikt = atomLista[i].getvikt()*mol.num
    if(not mol.next == None):
        vikt += weight(mol.next, atomLista)
    if(not mol.down == None):
        vikt += weight(mol.down, atomLista) * mol.num
    return vikt

def getEnd(q):
    tempStr = ""
    while (not q.peek() == None):
        character = q.dequeue()
        tempStr += character
    return tempStr

def readFormel(q):
    if(readMol(q) == False):
        #print("Formeln är syntaktiskt korrekt")
        return "Formeln är syntaktiskt korrekt", rutanFirst
    return error, rutanFirst



def readMol(q, inPa = False, rutan = None):
    boolGroup, rutan = readGroup(q, inPa, rutan)
    if(boolGroup == False):
        if(not q.peek() == None):
            if(not q.peek() == ")"):
                if(readMol(q, inPa, rutan) == False):
                    return False
                else:
                    return True
            else:
                if(inPa == True):
                    return False
                else:
                    if(readMol(q, inPa, rutan) == False):
                        return False
                    else:
                        return True
        else:
            return False
    return True

def readGroup(q, inPa, rutan):
    global rutanFirst
    if(rutan == None):
        rutan = Ruta()
    elif(rutan.atom == "( )" and rutan.num == 1):
        rutan.down = Ruta()
        rutan = rutan.down
    else:
        rutan.next = Ruta()
        rutan = rutan.next
    if(rutanFirst == None):
        rutanFirst = rutan
    global error
    tempStr = ""
    if q.peek() in nr:
        tempStr = getEnd(q)
        error = ("Felaktig gruppstart vid radslutet " + tempStr)
        return True, None
    if(q.peek() == "("):
        q.dequeue()
        inPa = True, None
        if(readMol(q, True, rutan) == False):
            if q.peek() == ")":
                q.dequeue()
                inPa = False
                if(not q.peek() == None):
                    boolNum, numInt = readNum(q)
                    if(boolNum == False):
                        rutan.num = int(numInt)
                        return False, rutan
                tempStr = getEnd(q)
                error = ("Saknad siffra vid radslutet " + tempStr)
                return True, None
            else:
                error = ("Saknad högerparentes vid radslutet")
        return True, None
    if(q.peek() == ")"):
        tempStr = getEnd(q)
        error = ("Felaktig gruppstart vid radslutet " + tempStr)
        return True, None

    boolAtom, atomStr = readAtom(q)
    if boolAtom == False:
        rutan.atom = atomStr
        if(not q.peek() == None and q.peek() in nr):
            boolNum, numInt = readNum(q)
            if (boolNum == False):
                rutan.num = int(numInt)
                if(not q.peek() == None and not q.peek() == ")"):
                    if(readMol(q, inPa, rutan) == True):
                        return True, None
                return False, rutan
            else:
                return True, None
        elif(not q.peek() == None and q.peek() == ")" and inPa == False):
            tempStr = getEnd(q)
            error = ("Felaktig gruppstart vid radslutet " + tempStr)
            return True, None
        elif(q.peek() == None):
            return False, rutan
        return False, rutan
    return True, None

def readAtom(q):
    global error
    tempAtomStr = ""
    tempStr = ""
    charH = readHighLetter(q)
    if(charH == True):
        return True, ""
    else:
        tempAtomStr += charH

    if not q.peek() in higher and not q.peek() in nr and not q.peek() == None and not q.peek() == ")" and not(q.peek() == "("):
        charL = readLowLetter(q)
        if (charL == True):
            return True, ""
        else:
            tempAtomStr += charL
    if(not tempAtomStr in atomer):
        tempStr = getEnd(q)
        #print("Okänd atom vid radslutet " + tempStr)
        error = "Okänd atom vid radslutet " + tempStr
        return True, ""
    return False, tempAtomStr

def readHighLetter(q):
    global error
    tempStr = ""
    character = q.dequeue()
    if (character in higher):
        return character
    tempStr += character
    tempStr += getEnd(q)

    #print("Saknad stor bokstav vid radslutet " + tempStr)
    error = ("Saknad stor bokstav vid radslutet " + tempStr)
    return True
    #   raise molekylException("Saknad stor bokstav vid radslutet " + tempStr)

def readLowLetter(q):
    global error
    tempList = []
    character = q.dequeue()
    if (character in lower):
        return character
    #print("Saknad liten bokstav vid radslutet")
    error = ("Saknad liten bokstav vid radslutet")
    return True
    raise molekylException("Saknad liten bokstav vid radslutet")

def readNum(q):
    global error
    tempList = ""
    tempStr = ""
    while (not q.peek() == None):
        character = q.peek()
        if (character in nr):
            tempList+=character
            q.dequeue()
        elif(len(tempList) == 0):
            return True, ""
        else:
            break

    if int(tempList[0]) == 0:
        #ex: if: atom0  else: atom0123
        if(len(tempList) == 1):
            tempStr += getEnd(q)
            #print("För litet tal vid radslutet " + tempStr)
            error = ("För litet tal vid radslutet " + tempStr)
            return True, ""
            raise molekylException("För litet tal vid radslutet")
        else:
            for i in range(len(tempList)-1):
                tempStr += tempList[i+1]
            tempStr += getEnd(q)
            #print("För litet tal vid radslutet " + tempStr)
            error = ("För litet tal vid radslutet " + tempStr)
            return True, ""
            raise molekylException("För litet tal vid radslutet " + tempStr)

    if (len(tempList) == 1 and int(tempList[0]) == 1):
        #ex: atom1
        tempStr = getEnd(q)
        #print("För litet tal vid radslutet " + tempStr)
        error = ("För litet tal vid radslutet " + tempStr)
        return True, ""
        raise molekylException("För litet tal vid radslutet")
    return False, tempList

# #unittest
# if __name__ == "__main__":
#     import unittest
#     class TestSyntax(unittest.TestCase):
#         def test_1(self):
#             q = LinkedQ()
#             ord = ("Si(C3(COOH)2)4(H2O)7")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Formeln är syntaktiskt korrekt")
#             ord = ("Na332")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Formeln är syntaktiskt korrekt")
#             ord = ("H2O")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Formeln är syntaktiskt korrekt")
#             ord = ("He")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Formeln är syntaktiskt korrekt")
#
#         def test_2(self):
#             q = LinkedQ()
#             ord = ("C(Xx4)5")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Okänd atom vid radslutet 4)5")
#             ord = ("C(OH4)C")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Saknad siffra vid radslutet C")
#             ord = ("C(OH4C")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Saknad högerparentes vid radslutet")
#             ord = ("H2O)Fe")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Felaktig gruppstart vid radslutet )Fe")
#             ord = ("H0")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "För litet tal vid radslutet ")
#             ord = ("H1C")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "För litet tal vid radslutet C")
#             ord = ("H02C")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "För litet tal vid radslutet 2C")
#             ord = ("Nacl")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Saknad stor bokstav vid radslutet cl")
#             ord = ("a")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Saknad stor bokstav vid radslutet a")
#             ord = ("(Cl)2)3")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Felaktig gruppstart vid radslutet )3")
#             ord = (")")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Felaktig gruppstart vid radslutet )")
#             ord = ("2")
#             for bokstav in ord.strip():
#                 q.enqueue(bokstav)
#             self.assertEqual(readFormel(q), "Felaktig gruppstart vid radslutet 2")
#
# if __name__ == "__main__":
#     unittest.main()

#Kattis
def main():
    atomlista = skapaAtomlista()
    mg = Molgrafik()
    from sys import stdin

    q = LinkedQ()
    for line in stdin:
        line = line.strip()
        value = line
        if value == '#':
            break
        elif len(value) != 0:
            for bokstav in value:
                q.enqueue(bokstav)
        molError, mol = readFormel(q)
        print(molError)
        print(weight(mol, atomlista))
        mg.show(mol)


if __name__ == "__main__":
    main()

# mol = Ruta(atom = "Cl", num=2)
# mg = Molgrafik()
# mg.show(mol)
