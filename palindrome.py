def removeit(str1):
        str2=str1.lower();
        i=0;
        strlen=len(str2);
        str3="";
        while (i<strlen):
                if not (str2[i] in [' ','\'','.',',','?',';',':']):
                    str3+=str2[i];
                i+=1;
        return str3;

def reverseit(str1):
        str3=removeit(str1);
        strlen3=len(str3)-1;
        str4="";
        while (strlen3>=0):
            str4+=str3[strlen3];
            strlen3-=1;
        return str4;

def ispalin(str1,str2):
    if (str1==str2):return True;
    else: return False;
    

sentence="Was it a rat I saw?";

print(ispalin(removeit(sentence),reverseit(sentence)));


            
        
