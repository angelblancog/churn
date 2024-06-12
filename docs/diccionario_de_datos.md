# **Diccionario de datos**

Este conjunto ha sido obtenido de la fuente:  

<a href="https://www.kaggle.com/datasets/blastchar/telco-customer-churn?resource=download" style="color: orange;">https://www.kaggle.com/datasets/blastchar/telco-customer-churn?resource=download</a>


### **Contexto:**

Se trata de un conjunto de datos diseñado por IBM para intentar predecir el comportamiento para retener clientes. Con él, se puede analizar todos los datos relevantes de los clientes y desarrollar programas centrados en la retención de clientes.


### **Resumen del contenido:**

Cada fila representa a un cliente, cada columna contiene atributos del cliente descritos en los metadatos de la columna.

El conjunto de datos incluye información sobre:

- Clientes que se fueron en el último mes: la columna se llama Churn.
- Servicios a los que se ha inscrito cada cliente: teléfono, líneas múltiples, internet, seguridad en línea, copia de seguridad en línea, protección de dispositivos, soporte técnico y televisión y películas en streaming.
- Información de la cuenta del cliente: cuánto tiempo han sido cliente, contrato, método de pago, facturación electrónica, cargos mensuales y cargos totales.
- Información demográfica sobre los clientes: género, rango de edad y si tienen parejas y dependientes.

### **Tamaño del conjunto de datos**

El conjunto de datos está compuesto por:

- 7.043 filas.

- 21 columnas.

### **Variables disponibles:**  

</br>

- Age: La edad actual del cliente, en años, al finalizar el trimestre fiscal.

- Churn: Yes = el cliente dejó la empresa este trimestre. No = el cliente se quedó con la empresa. 

- Contract: Indica el tipo de contrato actual del cliente: Month-to-Month (mensual), One Year (anual), Two Year (bianual).

- customerID: Un ID único que identifica a cada cliente. 

- Dependents: Indica si el cliente vive con dependientes: Yes, No. Los dependientes pueden ser hijos, padres, abuelos, etc.  

- DeviceProtection: Indica si el cliente tiene suscrito un servicio adicional de seguridad en línea proporcionado por la empresa: Yes, No.

- gender: El género del cliente: Male (Masculino), Female (Femenino).

- InternetService: Indica si el cliente tiene suscrito el servicio de Internet con la empresa: No, DSL, Fiber Optic (Fibra Óptica), Cable.

- Partner: Indica si el cliente está casado: Yes, No.

- MonthlyCharges: Indica el cargo mensual total actual del cliente por todos sus servicios de la empresa.  

- MultipleLines: Indica si el cliente tiene suscrito múltiples líneas telefónicas con la empresa: Yes, No.

- OnlineBackup: Indica si el cliente tiene suscrito un servicio adicional de copia de seguridad en línea proporcionado por la empresa: Yes, No.

- OnlineSecurity: Indica si el cliente tiene suscrito un plan adicional de protección de dispositivos para su equipo de Internet proporcionado por la empresa: Yes, No.

- PaperlessBilling: Indica si el cliente ha elegido la facturación electrónica: Yes, No.

- PaymentMethod: Indica cómo paga el cliente su factura: Bank Withdrawal (Retiro bancario), Credit Card (Tarjeta de crédito), Mailed Check (Cheque enviado por correo).  

- PhoneService: Indica si el cliente tiene suscrito el servicio telefónico residencial con la empresa: Yes, No.

- SeniorCitizen: Indica si el cliente tiene 65 años o más: Yes, No.  

- StreamingMovies: Indica si el cliente utiliza su servicio de Internet para transmitir películas de un proveedor externo: Yes, No. La empresa no cobra una tarifa adicional por este servicio.

- StreamingTV: Indica si el cliente utiliza su servicio de Internet para transmitir programación de televisión de un proveedor externo: Yes, No. La empresa no cobra una tarifa adicional por este servicio.

- TechSupport: Indica si el cliente tiene suscrito un plan adicional de soporte técnico de la empresa con tiempos de espera reducidos: Yes, No

- tenure: Indica el total de meses que el cliente ha estado con la empresa. 

- TotalCharges: Indica los cargos totales del cliente, calculados hasta el final del trimestre especificado anteriormente.


### **Variables por tipo:**

#### Binarias:

- Churn
- Dependents
- DeviceProtection
- Partner
- MultipleLines
- OnlineBackup
- OnlineSecurity
- PaperlessBilling
- PhoneService
- SeniorCitizen
- StreamingMovies
- StreamingTV
- TechSupport

#### Categóricas:

- Contract
- gender
- InternetService
- PaymentMethod

#### Numéricas:

- customerID
- MonthlyCharges
- tenure
- TotalCharges