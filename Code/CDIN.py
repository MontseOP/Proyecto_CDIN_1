# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:06:33 2021

@author: DELL
"""

import pandas as pd
import numpy as np
import string


class CDIN:
    
## Métodos para limpieza de datos    
    
    def remover_punctuation(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.punctuation)
        except:
            pass
        return x
    
        
    def remove_digits(x):
        try:
           x = ''.join(ch for ch in x if ch not in string.digits)
        except:
            pass
        return x
    
    def remove_whitespace(x):
        try:
            x = ''.join(x.split())
        except:
            pass
        return x
    
    def replace_text(x, to_replace, replacement):
        try:
            x = x.replace(to_replace, replacement)
        except:
            pass
        return x

    def lowercase_text(x):
        try:
            x = x.lower()
        except:
            pass
        return x
    
    def uppercase_text(x):
        try:
            x = x.upper()
        except:
            pass
        return x
    
    def remove_whitespace_lr(x):
        try:
            x = x.lstrip().rstrip()
        except:
            pass
        return x

#data quality report: dqr
    def dqr(data):
       
        #Lista de variables de lista de datos
        columns = pd.DataFrame(list(data.columns.values), columns=['Nombres'], index=list(data.columns.values))
        
        #Lista de tipos de datos
        data_types = pd.DataFrame(data.dtypes, columns=['Tipo_dato'])
        
        #Lista de valores perdidos
        missing_values = pd.DataFrame(data.isnull().sum(), columns=['Datos_faltantes'])
        
        #Lista de valores únicos
        unique_values = pd.DataFrame(columns=['Valores_únicos'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]
        
        #Promedio de valores numéricos
        mean_values = pd.DataFrame(columns=['Promedio'])
        for col in list(data.columns.values):
            try:
                mean_values.loc[col] = [data[col].mean()]
            except:
                pass
            
        #Lista de valores mínimos
        min_values = pd.DataFrame(columns=['Valor_mínimo'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except:
                pass
            
        #Lista de valores máximos
        max_values = pd.DataFrame(columns=['Valor_máximo'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except:
                pass
        
        #Columna que se llame categórica (tipo booleana) que cuando sea True, represente una variable categórica, pero que cuando sea False sea una variable numérica
        categorical = pd.DataFrame(columns=['Categorical'])
        for col in list(data.columns.values):
            if data[col].dtype == 'object':
                categorical.loc[col] = True
            else: 
                categorical.loc[col] = False
        
        return columns.join(data_types).join(missing_values).join(unique_values).join(mean_values).join(min_values).join(max_values).join(categorical)
        
    
    def get_dummies_nom (df, cat_nominales):
    
       df_nom_dummy= pd.get_dummies(df[cat_nominales[0]], prefix=cat_nominales[0])

       for col in cat_nominales[1:]:
         temp =  pd.get_dummies(df[col], prefix=col)
         df_nom_dummy = df_nom_dummy.join(temp)

       return df_nom_dummy   
    
    
    
    
    
    
    
    
    
    
    
    
    