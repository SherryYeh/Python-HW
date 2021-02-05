void Add(char *ch1, char *ch2, char *ch3){
    int len1=strlen(ch1),len2=strlen(ch2),i,tmp,num1[],num2[],num3[];
    memset(num1 , 0 , sizeof(num1));
    memset(num2 , 0 , sizeof(num2));
    memset(num3 , 0 , sizeof(num3));
    for (i=len1-1;i>=0;i--) num1[len1-1-i] = ch1[i]-'0';
    for (i=len2-1;i>=0;i--) num2[len2-1-i] = ch2[i]-'0';
    i=0;
    while (i<len1) {
        tmp = 0;
        num3[i] = num1[i]+num2[i]+tmp;
        if (num3[i]>=10) {
            tmp = num3[i]/10;
            num3[i]%=10;
        }
        i++;
    }
    if (tmp!=0){
        num3[i]=tmp;
        i++;
    }
    len1 = i;
    for (i=len1-1;i>=0;i--) ch3[len1-1-i] = num3[i]+'0';
    ch3[len1] = 0;
}



int len1=strlen(a),len2=strlen(b),i,k=0,j,carry=0,kk=0,t;
for (i=0;i<60;i++)
    c[i]='0';
c[60-1]=0;printf("A=%d\n",c[59]);
for (i=len1-1;i>=0;i--,k++) {
    for(j=len2-1,kk=0;j>=0;j--,kk++) {
        t=((a[i]-'0')*(b[j]-'0')+carry+(c[60-2-k-kk]-'0'))%10+'0';printf("T=%d\n",t);
        carry=((a[i]-'0')*(b[j]-'0')+carry+(c[60-2-k-kk]-'0'))/10;
        c[60-2-k-kk]=t;
        if (j==0)
            {c[60-3-k-kk]='0'+s;s=0;}
    }
}
if(c[60-len1-len2-1]=='0')
    k=len1+len2-1;
else
    k=len1+len2;
for(i=0;i<k;i++)
    c[i]=c[i+60-k-1];
c[k]=0;
}

