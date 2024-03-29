# Generated from SCLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SCLangParser import SCLangParser
else:
    from SCLangParser import SCLangParser

# This class defines a complete generic visitor for a parse tree produced by SCLangParser.

class SCLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SCLangParser#script.
    def visitScript(self, ctx:SCLangParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#definition.
    def visitDefinition(self, ctx:SCLangParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#conditionBlock.
    def visitConditionBlock(self, ctx:SCLangParser.ConditionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#visibility.
    def visitVisibility(self, ctx:SCLangParser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#actionBlock.
    def visitActionBlock(self, ctx:SCLangParser.ActionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#effectBlock.
    def visitEffectBlock(self, ctx:SCLangParser.EffectBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#metaData.
    def visitMetaData(self, ctx:SCLangParser.MetaDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#logicExpr.
    def visitLogicExpr(self, ctx:SCLangParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#logicTerm.
    def visitLogicTerm(self, ctx:SCLangParser.LogicTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#logicGroup.
    def visitLogicGroup(self, ctx:SCLangParser.LogicGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#logicOr.
    def visitLogicOr(self, ctx:SCLangParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#logicAnd.
    def visitLogicAnd(self, ctx:SCLangParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#liveTerm.
    def visitLiveTerm(self, ctx:SCLangParser.LiveTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#modifier.
    def visitModifier(self, ctx:SCLangParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#comparison.
    def visitComparison(self, ctx:SCLangParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#compareOp.
    def visitCompareOp(self, ctx:SCLangParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#entityRef.
    def visitEntityRef(self, ctx:SCLangParser.EntityRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#entityGroup.
    def visitEntityGroup(self, ctx:SCLangParser.EntityGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#entityDef.
    def visitEntityDef(self, ctx:SCLangParser.EntityDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#entityType.
    def visitEntityType(self, ctx:SCLangParser.EntityTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#entityClass.
    def visitEntityClass(self, ctx:SCLangParser.EntityClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#entityVariable.
    def visitEntityVariable(self, ctx:SCLangParser.EntityVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#entityConstant.
    def visitEntityConstant(self, ctx:SCLangParser.EntityConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#dataType.
    def visitDataType(self, ctx:SCLangParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#attrib.
    def visitAttrib(self, ctx:SCLangParser.AttribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#methodCall.
    def visitMethodCall(self, ctx:SCLangParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#argsWrapper.
    def visitArgsWrapper(self, ctx:SCLangParser.ArgsWrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#argsList.
    def visitArgsList(self, ctx:SCLangParser.ArgsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#argument.
    def visitArgument(self, ctx:SCLangParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#metaBlock.
    def visitMetaBlock(self, ctx:SCLangParser.MetaBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#metaEntry.
    def visitMetaEntry(self, ctx:SCLangParser.MetaEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#value.
    def visitValue(self, ctx:SCLangParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#entity.
    def visitEntity(self, ctx:SCLangParser.EntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCLangParser#method.
    def visitMethod(self, ctx:SCLangParser.MethodContext):
        return self.visitChildren(ctx)



del SCLangParser