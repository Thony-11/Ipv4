import re

class Function:
    def __init__(self):
        pass

    def nbre_adress_dispobible(self,cidr):
        puissance = ((32-int(cidr))-2)
        return pow(2,puissance)

    def binary_to_int(self,value):
        response = int(value,2)
        return response

    def to_binary(self,value):
        response = '{:08b}'.format(int(value))
        return response

    def replace_str_index(self,text,index,value):
        return text[:index] + value + text[index+1:]

    def replace_value_to_0(self,string_binary,cidr):
        while cidr < 32:
            repl = self.replace_str_index(string_binary,cidr,'0')
            string_binary = repl
            cidr = cidr + 1
        return string_binary

    def replace_value_to_11(self,string_binary,cidr):
        while cidr < 32:
            repl = self.replace_str_index(string_binary,cidr,'1')
            string_binary = repl
            cidr = cidr + 1
        return string_binary

    def replace_value_to_1(self,string_binary,cidr):
        index = 0
        while index < cidr:
            repl = self.replace_str_index(string_binary,index,'1')
            string_binary = repl
            index = index + 1
        return string_binary

    def _ipv4_with_class(self,string_ipv4):
        info=[]
        response = ''
        x = string_ipv4.split('.')
        first_octet =  int(x[0])
        if(first_octet>=0  and first_octet<=127):
            response = 'A'
            adress_reseaux = str(first_octet)+'.0.0.0'
            adress_diff = str(first_octet)+'.255.255.255'
            first_adress = str(first_octet)+'.0.0.1'
            last_adress = str(first_octet)+'.255.255.254'
            masque = '255.0.0.0'
            nbre = pow(2,(24-2))
            info.append(string_ipv4)
            info.append(response)
            info.append(masque)
            info.append(adress_reseaux)
            info.append(adress_diff)
            info.append(first_adress)
            info.append(last_adress)
            info.append(nbre)
        if(first_octet>=128  and first_octet<=191):
            response = 'B'
            adress_reseaux = str(first_octet)+'.'+str(x[1])+'.0.0'
            adress_diff = str(first_octet)+'.'+str(x[1])+'.255.255'
            first_adress = str(first_octet)+'.'+str(x[1])+'.0.1'
            last_adress = str(first_octet)+'.'+str(x[1])+'.255.254'
            masque = '255.255.0.0'
            nbre = pow(2,(16-2))
            info.append(string_ipv4)
            info.append(response)
            info.append(masque)
            info.append(adress_reseaux)
            info.append(adress_diff)
            info.append(first_adress)
            info.append(last_adress)
            info.append(nbre)
        if(first_octet>=192  and first_octet<=223):
            response = 'C'
            adress_reseaux = str(first_octet)+'.'+str(x[1])+'.'+str(x[2])+'.0'
            adress_diff = str(first_octet)+'.'+str(x[1])+'.'+str(x[2])+'.255'
            first_adress = str(first_octet)+'.'+str(x[1])+'.'+str(x[2])+'.1'
            last_adress =  str(first_octet)+'.'+str(x[1])+'.'+str(x[2])+'.254'
            masque = '255.255.255.0'
            nbre = pow(2,(8-2))
            info.append(string_ipv4)
            info.append(response)
            info.append(masque)
            info.append(adress_reseaux)
            info.append(adress_diff)
            info.append(first_adress)
            info.append(last_adress)
            info.append(nbre)
        if(first_octet>=224  and first_octet<=239):
            response = 'D'
            adress_reseaux = string_ipv4
            adress_diff ='no define'
            first_adress = str(first_octet)+'.'+str(x[1])+'.'+str(x[2])+str(x[3]+1)
            last_adress =  str(first_octet)+'.'+str(x[1])+'.'+str(x[2])+str(x[3]-1)
            masque = '255.255.255.255'
            nbre = 'no define'
            info.append(string_ipv4)
            info.append(response)
            info.append(masque)
            info.append(adress_reseaux)
            info.append(adress_diff)
            info.append(first_adress)
            info.append(last_adress)
            info.append(nbre)
        if(first_octet>=240  and first_octet<=255):
            response = 'E'
            adress_reseaux = string_ipv4
            adress_diff ='no define'
            first_adress = str(first_octet)+'.'+str(x[1])+'.'+str(x[2])+str(x[3]+1)
            last_adress =  str(first_octet)+'.'+str(x[1])+'.'+str(x[2])+str(x[3]-1)
            masque = 'no define'
            nbre = 'no define'
            info.append(string_ipv4)
            info.append(response)
            info.append(masque)
            info.append(adress_reseaux)
            info.append(adress_diff)
            info.append(first_adress)
            info.append(last_adress)
            info.append(nbre)
        return info

    def _ipv4_no_class(self,string_ip,cidr):
        binary=[]
        response=[]
        x = string_ip.split('.')
        adress_disponible= self.nbre_adress_dispobible(cidr)
        for i in range(len(x)):
            binary.append(self.to_binary(x[i]))
        
        # ////Calcule Masque Sous Reseau
        concat_bin = binary[0]+""+binary[1]+""+binary[2]+""+binary[3]
        concat_bin = self.replace_value_to_1(concat_bin,cidr)
        concat_bin = self.replace_value_to_0(concat_bin,cidr)
        str_masque = str(self.binary_to_int(concat_bin[0:8]))+'.'+str(self.binary_to_int(concat_bin[8:16]))+'.'+str(self.binary_to_int(concat_bin[16:24]))+'.'+str(self.binary_to_int(concat_bin[24:32]))
        # print(str_masque)

        # /////Calcule Adress Reseaux
        adress_reseaux_bin = binary[0]+""+binary[1]+""+binary[2]+""+binary[3]
        adress_reseaux_bin = self.replace_value_to_0(adress_reseaux_bin,cidr)
        str_reseaux = str(self.binary_to_int(adress_reseaux_bin[0:8]))+'.'+str(self.binary_to_int(adress_reseaux_bin[8:16]))+'.'+str(self.binary_to_int(adress_reseaux_bin[16:24]))+'.'+str(self.binary_to_int(adress_reseaux_bin[24:32]))
        
        # ////Calcule 1er Adresse disponible
        first_adress = str(self.binary_to_int(adress_reseaux_bin[0:8]))+'.'+str(self.binary_to_int(adress_reseaux_bin[8:16]))+'.'+str(self.binary_to_int(adress_reseaux_bin[16:24]))+'.'+str(self.binary_to_int(adress_reseaux_bin[24:32])+1)



        # /////Calcule Adress Diffusion
        adress_diff_bin = binary[0]+""+binary[1]+""+binary[2]+""+binary[3]
        adress_diff_bin = self.replace_value_to_11(adress_diff_bin,cidr)
        str_diffusion = str(self.binary_to_int(adress_diff_bin[0:8]))+'.'+str(self.binary_to_int(adress_diff_bin[8:16]))+'.'+str(self.binary_to_int(adress_diff_bin[16:24]))+'.'+str(self.binary_to_int(adress_diff_bin[24:32]))
        
        # ////Calcule dernier Adresse disponible
        last_adress = str(self.binary_to_int(adress_diff_bin[0:8]))+'.'+str(self.binary_to_int(adress_diff_bin[8:16]))+'.'+str(self.binary_to_int(adress_diff_bin[16:24]))+'.'+str(self.binary_to_int(adress_diff_bin[24:32])-1)


        response.append(string_ip)
        response.append(str_masque)
        response.append(str_reseaux)
        response.append(str_diffusion)
        response.append(first_adress)
        response.append(last_adress)
        response.append(self.nbre_adress_dispobible(cidr))

        return response

