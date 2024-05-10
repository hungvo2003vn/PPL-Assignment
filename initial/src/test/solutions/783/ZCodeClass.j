.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public <init>()V
Label0:
.var 0 is this LZCodeClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	return
Label1:
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is a Ljava/lang/Object; from Label2 to Label3
	ldc 1.0000
	fstore_2
	fload_2
	ldc 0.0000
	fcmpl
	ifeq Label8
	iconst_0
	goto Label9
Label8:
	iconst_1
Label9:
	ifle Label7
	ldc 1.0000
	invokestatic io/writeNumber(F)V
	goto Label6
Label7:
	fload_2
	ldc 1.0000
	fcmpl
	ifeq Label11
	iconst_0
	goto Label12
Label11:
	iconst_1
Label12:
	ifle Label10
	ldc 2.0000
	invokestatic io/writeNumber(F)V
	goto Label6
Label10:
	fload_2
	ldc 2.0000
	fcmpl
	ifeq Label14
	iconst_0
	goto Label15
Label14:
	iconst_1
Label15:
	ifle Label13
	ldc 3.0000
	invokestatic io/writeNumber(F)V
	goto Label6
Label13:
Label6:
Label3:
	return
Label1:
.limit stack 2
.limit locals 3
.end method
