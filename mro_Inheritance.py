"""
class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass
print(M.mro())
"""

class A(object): pass
class B(object): pass
class C(A): pass
class D(A): pass
class E(C, D): pass
class F(B): pass
class G(B): pass
class H(F, G): pass
class I(E, H): pass

print(I.mro())