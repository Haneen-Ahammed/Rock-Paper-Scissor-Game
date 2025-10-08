Target code generator 

#include<stdio.h>
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
