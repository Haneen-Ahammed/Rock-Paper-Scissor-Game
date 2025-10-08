Target code generator 

#include<stdio.h>![IMG-20251008-WA0009](https://github.com/user-attachments/assets/d8891ed5-3e34-4828-86df-0cf5b99dbb8d)
![IMG-20251008-WA0008](https://github.com/user-attachments/assets/cdf030d1-d1a6-4bce-a229-817a38052805)

#include<string.h>

char op[2], arg1[5], arg2[5], result[5];

int main(){
    FILE *f1,*f2;
    f1=fopen("input1.txt","r");
    f2=fopen("output1.txt","w");
    fscanf(f1,"%s%s%s%s",op,arg1,arg2,result);
    while(!feof(f1)){
        if(strcmp(op,"+")==0){
           fprintf(f2,"\nMOV R0,%s",arg1);
           fprintf(f2,"\nADD R0,%s",arg2);
           fprintf(f2,"\nMOV %s,R0",result);
        }
        if(strcmp(op,"*")==0){
           fprintf(f2,"\nMOV R0,%s",arg1);
           fprintf(f2,"\nMUL R0,%s",arg2);
           fprintf(f2,"\nMOV %s,R0",result);
        }
        if(strcmp(op,"-")==0){
           fprintf(f2,"\nMOV R0,%s",arg1);
           fprintf(f2,"\nSUB R0,%s",arg2);
           fprintf(f2,"\nMOV %s,R0",result);
        }
        if(strcmp(op,"/")==0){
           fprintf(f2,"\nMOV R0,%s",arg1);
           fprintf(f2,"\nDIV R0,%s",arg2);
           fprintf(f2,"\nMOV %s,R0",result);
        }
        if(strcmp(op,"=")==0){
           fprintf(f2,"\nMOV R0,%s",arg1);
           fprintf(f2,"\nMOV %s,R0",result);
        }
        fscanf(f1,"%s%s%s%s",op,arg1,arg2,result);
    }
    fclose(f1); fclose(f2);
    return 0;
}

expression evaluation 

lex

%{
#include "y.tab.h"
#include<stdio.h>
extern int yylval;
%}
%%
[0-9]+ { yylval = atoi(yytext); return num; }
\n { return 0; }
. { return yytext[0]; }
%%

yacc

%{
#include<stdio.h>
#include<stdlib.h>
int f=0;
%}
%token num
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'
%%
arexp: exp { printf("result= %d\n", $1); return 0; };
exp: exp '+' exp { $$ = $1 + $3; }
   | exp '-' exp { $$ = $1 - $3; }
   | exp '*' exp { $$ = $1 * $3; }
   | exp '/' exp { $$ = $1 / $3; }
   | '(' exp ')' { $$ = $2; }
   | num { $$ = $1; }
;
%%
int main(){
  printf("Enter: \n");
  yyparse();
  if(f==0)
    printf("valid \n");
}
int yyerror(){
  printf("invalid\n");
  f=1;
  exit(0);
}

lexical anayalicer

%{
#include<stdio.h>
%}

%%
"if"|"else"|"while"|"for"|"switch"|"break"|"continue"|"do"    {printf("%s is a Keyword\n", yytext);}
"||"|"&&"                                                      {printf("%s is a Logical operator\n", yytext);}
[A-Za-z][A-Za-z0-9]*                                           {printf("%s is an Identifier\n", yytext);}
[0-9]+                                                         {printf("%s is a Number\n", yytext);}
"=="|"!="|"<="|">="|"<"|">"                                   {printf("%s is a Relational operator\n", yytext);}
"*"|"/"|"+"|"-"|"%"                                           {printf("%s is an Arithmetic operator\n", yytext);}
"="                                                            {printf("%s is an Assignment operator\n", yytext);}
"++"                                                           {printf("%s is an Increment operator\n", yytext);}
"--"                                                           {printf("%s is a Decrement operator\n", yytext);}
.                                                              {printf("%s is Invalid\n", yytext);}
%%

int main(int argc, char *argv[])
{
    yyin = fopen(argv[1], "r");
    yylex();
}


word

%{ #include<stdio.h> 
int words=0,ch=0,line=0; 
%} 
%% 
[A-Z|a-z]" " {words++;ch++;} 
[A-Z|a-z]"\n" {words++;ch++;line++;} 
[A-Z|a-z] {ch++;}
 "." {printf("No of words:%d\nNo of characters:%d\nNo of lines:%d\n",words,ch,line);}
 . {} 
%% 
int main{
printf("enter");
yylex(); 
return 0;}

Rdp

#include<stdio.h>

#include<string.h>

#include<ctype.h>

char input[20];

int i=0,error=0;

void E();

void T();

void Eprime();

void Tprime();

void F();

void main(){

printf("Enter an arithmetic expression: \n");

gets(input);

E();

if(strlen(input)==i && error==0)

printf("Accepted....!!\n");

else

printf("Rejected....!!\n");

}

void E(){

T();

Eprime();

}

void Eprime(){

if(input[i]=='+')

{

i++;

T();

Eprime();

}

}

void T(){

F();

Tprime();

}

void Tprime(){

if(input[i]=='*'){

i++;

F();

Tprime();

}

}

void F(){

if(isalnum(input[i]))

i++;
else if(input[i]=='('){

i++;

E();

if(input[i]==')')

i++;

else

error=1;

}

else

error=1;

}

Output

Enter an arithmetic expression:

a+b*c

Accepted....!!

Enter an arithmetic expression:

a++b

Rejected....!
