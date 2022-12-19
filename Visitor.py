from turtle3d import Turtle3D
if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
    from .logo3dVisitor import logo3dVisitor
else:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor


class Visitor(logo3dVisitor):
    def __init__(self, funcname, param):
        self.var = {}
        self.func = {}
        self.inifunc = funcname
        self.iniparam = param
        self.tortuga = None

    def iniExec(self):
        print('Executing program...')
        param = self.func[self.inifunc]
        for i in range(0, len(param)-1):
            self.var[param[i]] = self.iniparam[i]
        self.visit(param[len(param)-1])

    def visitRoot(self, ctx):
        return self.visitChildren(ctx)

    def visitFunc(self, ctx):
        l = list(ctx.getChildren())
        param = [l[len(l)-2]]
        if len(l) > 7:
            for i in range(len(l)-5, 2, -2):
                param.insert(0, l[i].getText())
        error = self.func.get(l[1].getText())
        if error is None:
            self.func[l[1].getText()] = param
        else:
            raise Exception('Procediment ja definit!')

    def visitBlInstr(self, ctx):
        return self.visitChildren(ctx)

    def visitAsignacio(self, ctx):
        l = list(ctx.getChildren())
        self.var[l[0].getText()] = self.visit(l[2])

    def visitEntrada(self, ctx):
        l = list(ctx.getChildren())
        self.var[l[1].getText()] = float(input(''))

    def visitSortida(self, ctx):
        l = list(ctx.getChildren())
        print(str(self.visit(l[1])))

    def visitBlocIfElse(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            self.visit(l[3])
        else:
            if len(l) > 5:
                self.visit(l[5])

    def visitBlocWhile(self, ctx):
        l = list(ctx.getChildren())
        while(self.visit(l[1])):
            self.visit(l[3])

    def visitBlocFor(self, ctx):
        l = list(ctx.getChildren())
        varone = self.visit(l[3])
        varto = self.visit(l[5])
        if varone < varto:
            varfrom = varone
        else:
            varfrom = varto
            varto = varone
        self.var[l[1].getText()] = varfrom
        while self.var[l[1].getText()] <= varto:
            self.visit(l[7])
            self.var[l[1].getText()] += 1

    def visitFuncions(self, ctx):
        l = list(ctx.getChildren())
        funcio = l[0].getText()
        param = self.func.get(funcio)
        if param is not None:
            if len(l) > 3:
                valor = []
                for i in range(2, len(l)-1, 2):
                    valor.append(self.visit(l[i]))
                if len(valor) != len(param)-1:
                    raise Exception('Nombre de paràmetres incorrecte!')
                copy = self.var
                self.var = {}
                for i in range(0, len(param)-1):
                    self.var[param[i]] = valor[i]
                self.visit(param[len(param)-1])
                self.var = copy
        else:
            raise Exception('Procediment no definit!')

    def visitParentesi(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    def visitVariable(self, ctx):
        l = list(ctx.getChildren())
        self.var.setdefault(l[0].getText(), 0.0)
        return float(self.var[l[0].getText()])

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return float(l[0].getText())

    def visitSumaResta(self, ctx):
        l = list(ctx.getChildren())
        v1 = float(self.visit(l[0]))
        v2 = float(self.visit(l[2]))
        if l[1].getText() == '+':
            return v1 + v2
        else:
            return v1 - v2

    def visitMultDiv(self, ctx):
        l = list(ctx.getChildren())
        v1 = float(self.visit(l[0]))
        v2 = float(self.visit(l[2]))
        if l[1].getText() == '*':
            return v1 * v2
        else:
            if v2 == 0:
                raise Exception('No es pot dividir entre 0!')
            else:
                return v1 / v2

    def visitIgual(self, ctx):
        l = list(ctx.getChildren())
        v1 = float(self.visit(l[0]))
        v2 = float(self.visit(l[2]))
        return v1 == v2

    def visitDiferent(self, ctx):
        l = list(ctx.getChildren())
        v1 = float(self.visit(l[0]))
        v2 = float(self.visit(l[2]))
        return v1 != v2

    def visitMenysque(self, ctx):
        l = list(ctx.getChildren())
        v1 = float(self.visit(l[0]))
        v2 = float(self.visit(l[2]))
        return v1 < v2

    def visitMesque(self, ctx):
        l = list(ctx.getChildren())
        v1 = float(self.visit(l[0]))
        v2 = float(self.visit(l[2]))
        return v1 > v2

    def visitMenysEq(self, ctx):
        l = list(ctx.getChildren())
        v1 = float(self.visit(l[0]))
        v2 = float(self.visit(l[2]))
        return v1 <= v2

    def visitMesEq(self, ctx):
        l = list(ctx.getChildren())
        v1 = float(self.visit(l[0]))
        v2 = float(self.visit(l[2]))
        return v1 >= v2

    def visitTortuga(self, ctx):
        if self.tortuga is None:
            self.tortuga = Turtle3D()
        return self.visitChildren(ctx)

    def visitColor(self, ctx):
        l = list(ctx.getChildren())
        R = float(self.visit(l[2]))
        G = float(self.visit(l[4]))
        B = float(self.visit(l[6]))
        self.tortuga.color(R, G, B)

    def visitLeft(self, ctx):
        l = list(ctx.getChildren())
        p = float(self.visit(l[2]))
        self.tortuga.left(p)

    def visitRight(self, ctx):
        l = list(ctx.getChildren())
        p = float(self.visit(l[2]))
        self.tortuga.right(p)

    def visitUp(self, ctx):
        l = list(ctx.getChildren())
        p = float(self.visit(l[2]))
        self.tortuga.up(p)

    def visitDown(self, ctx):
        l = list(ctx.getChildren())
        p = float(self.visit(l[2]))
        self.tortuga.down(p)

    def visitForward(self, ctx):
        l = list(ctx.getChildren())
        p = float(self.visit(l[2]))
        self.tortuga.forward(p)

    def visitBackward(self, ctx):
        l = list(ctx.getChildren())
        p = float(self.visit(l[2]))
        self.tortuga.backward(p)

    def visitHide(self, ctx):
        self.tortuga.hide()

    def visitShow(self, ctx):
        self.tortuga.show()

    def visitHome(self, ctx):
        self.tortuga.home()

    def visitRadius(self, ctx):
        l = list(ctx.getChildren())
        p = float(self.visit(l[2]))
        self.tortuga.radius(p)
