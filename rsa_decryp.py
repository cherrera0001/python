#!/usr/bin/python
## RSA - Given p,q and e.. recover and use private key w/ Extended Euclidean Algorithm - crypto150-what_is_this_encryption @ alexctf 2017
# @author intrd - http://dann.com.br/ (original script here: http://crypto.stackexchange.com/questions/19444/rsa-given-q-p-and-e)
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

import binascii, base64
#reemplace cada uno de los parametros siguientes para poder decifrar 
#The encryption is RSA, and was given to us
#p = first prime number
#q = second prime number
#e = public/encryption exponent
#ct = ciphertext (encrypted text)

p  =  7493025776465062819629921475535241674460826792785520881387158343265274170009282504884941039852933109163193651830303308312565580445669284847225535166520307
q  =  7020854527787566735458858381555452648322845008266612906844847937070333480373963284146649074252278753696897245898433245929775591091774274652021374143174079
e  =  30802007917952508422792869021689193927485016332713622527025219105154254472344627284947779726280995431947454292782426313255523137610532323813714483639434257536830062768286377920010841850346837238015571464755074669373110411870331706974573498912126641409821855678581804467608824177508976254759319210955977053997
ct  =  44641914821074071930297814589851746700593470770417111804648920018396305246956127337150936081144106405284134845851392541080862652386840869768622438038690803472550278042463029816028777378141217023336710545449512973950591755053735796799773369044083673911035030605581144977552865771395578778515514288930832915182

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

n = p*q #product of primes
phi = (p-1)*(q-1) #modular multiplicative inverse
gcd, a, b = egcd(e, phi) #calling extended euclidean algorithm
d = a #a is decryption key

out = hex(d)
print("d_hex: " + str(out));
print("n_dec: " + str(d));

pt = pow(ct, d, n)
print("pt_dec: " + str(pt))

out = hex(pt)
out = str(out[2:-1])
print "flag"
print out.decode("hex")
