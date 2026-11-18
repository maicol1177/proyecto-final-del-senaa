## 1. Introducción

### 1.1 Propósito
Este documento especifica los requisitos funcionales y no funcionales de **Licores Connect**, un software web de gestión de ventas e inventario para pequeños y medianos comercios de licores en Colombia. Está dirigido al equipo de desarrollo, al instructor evaluador, a los negocios piloto y a cualquier persona que participe en el diseño, las pruebas o el mantenimiento del sistema[cite: 1].

### 1.2 Alcance
Licores Connect es una aplicación web en la nube, ofrecida bajo modelo SaaS (suscripción mensual o anual), que permite a licorerías, estancos, tiendas de barrio, minimercados y emprendedores[cite: 1]:
* Registrar ventas de forma rápida y generar la facturación correspondiente[cite: 1].
* Controlar automáticamente el stock de botellas y bebidas[cite: 1].
* Realizar el cuadre de caja diario[cite: 1].
* Consultar reportes financieros y de inventario en tiempo real[cite: 1].
* Administrar usuarios y permisos del negocio[cite: 1].

*Fuera del alcance de la versión 1.0:* facturación electrónica ante la DIAN, contabilidad completa, nómina, domicilios y tienda en línea para el consumidor final (ver sección 7, supuestos y riesgos)[cite: 1].

### 1.3 Definiciones, acrónimos y abreviaturas

| Término | Definición |
| :--- | :--- |
| **SRS** | Software Requirements Specification (Especificación de Requisitos de Software)[cite: 1] |
| **SaaS** | Software como servicio, accedido por suscripción desde el navegador[cite: 1] |
| **Stock** | Cantidad disponible de cada producto en inventario[cite: 1] |
| **SKU** | Código único que identifica un producto[cite: 1] |
| **Cuadre de caja** | Conciliación entre las ventas registradas y el dinero efectivamente recibido[cite: 1] |
| **Negocio / cliente** | Comercio suscrito a Licores Connect[cite: 1] |
| **Administrador** | Dueño o encargado con control total del negocio dentro del sistema[cite: 1] |
| **Vendedor** | Empleado que registra ventas[cite: 1] |
| **PSE** | Pagos Seguros en Línea[cite: 1] |
| **ADSO** | Análisis y Desarrollo de Software (SENA)[cite: 1] |
| **RF / RNF** | Requisito funcional / Requisito no funcional[cite: 1] |

### 1.4 Referencias
* Documento del proyecto productivo SENA: Planteamiento y delimitación del problema (componente Exploración)[cite: 1].
* Modelo de negocio CANVAS (componente Ideación)[cite: 1].
* IEEE Std 830-1998, práctica recomendada para especificaciones de requisitos de software (usada como guía de estructura)[cite: 1].

### 1.5 Visión general del documento
La sección 2 describe el producto en términos generales; la sección 3 detalla los requisitos funcionales; la sección 4, los no funcionales; la sección 5, las interfaces; la sección 6, los criterios de aceptación; y la sección 7, supuestos, restricciones y riesgos[cite: 1].

---

## 2. Descripción general

### 2.1 Contexto y problema
En Colombia, muchos pequeños y medianos comercios de licores llevan sus ventas e inventarios en libretas, cuadernos u hojas de cálculo básicas. Esto genera desorden administrativo, pérdida de tiempo en el registro diario, errores de facturación y de cuadre de caja, descuadres de inventario y ausencia de reportes en tiempo real para conocer las ganancias reales y decidir mejor[cite: 1].

### 2.2 Perspectiva del producto
Licores Connect es un producto independiente, accesible desde cualquier navegador con conexión a internet, sin instalaciones complicadas. Se integra con pasarelas de pago en línea para el cobro de suscripciones. Su diferenciador es ser intuitivo (sin requerir conocimientos técnicos), económico y especializado en licores y bebidas[cite: 1].

### 2.3 Funciones principales del producto
* Módulo de ventas: registro rápido, facturación y cuadre de caja[cite: 1].
* Módulo de inventario de licores: catálogo, stock automático y alertas[cite: 1].
* Módulo de reportes: ganancias, ventas e inventario en tiempo real[cite: 1].
* Módulo de usuarios: roles, permisos y gestión de cuentas[cite: 1].
* Módulo de suscripción y pagos: planes, cobro y estado de la cuenta[cite: 1].
* Soporte y demostración: acceso a una versión de prueba gratuita[cite: 1].

### 2.4 Clases de usuarios y características

| Usuario | Descripción | Nivel técnico |
| :--- | :--- | :--- |
| **Administrador del negocio** | Dueño o encargado. Configura el negocio, gestiona inventario, usuarios, reportes y suscripción[cite: 1]. | Bajo[cite: 1] |
| **Vendedor / cajero** | Registra ventas y consulta disponibilidad de productos[cite: 1]. | Bajo[cite: 1] |
| **Emprendedor nuevo** | Administrador que empieza su negocio y necesita organizarse desde el primer día[cite: 1]. | Bajo[cite: 1] |
| **Soporte Licores Connect** | Equipo desarrollador que atiende incidencias y administra cuentas de clientes[cite: 1]. | Alto[cite: 1] |

### 2.5 Entorno operativo
* Aplicación web alojada en servidores en la nube (hosting) con dominio propio[cite: 1].
* Compatible con navegadores modernos (Chrome, Edge, Firefox, Safari) en computador, tableta y celular[cite: 1].
* Requiere conexión a internet estable[cite: 1].

### 2.6 Restricciones de diseño e implementación
* Desarrollo por un equipo de 5 estudiantes bajo metodologías ágiles[cite: 1].
* Presupuesto limitado: uso de hosting económico y herramientas de desarrollo web modernas[cite: 1].
* Los precios del servicio deben ser accesibles para pequeños comercios[cite: 1].
* Cumplimiento de la normativa colombiana de protección de datos personales (Ley 1581 de 2012)[cite: 1].

### 2.7 Supuestos y dependencias
* Los negocios cuentan con al menos un dispositivo con internet en el punto de venta[cite: 1].
* Dependencia de proveedores externos de hosting, dominio y pasarelas de pago[cite: 1].
* Disponibilidad de licorerías piloto para validar el software[cite: 1].

---

## 3. Requisitos funcionales

*Prioridad:* Alta (imprescindible para la versión 1.0), Media (importante, puede entrar en un segundo ciclo) y Baja (deseable)[cite: 1].

### 3.1 Autenticación y gestión de usuarios

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-01** | El sistema debe permitir registrar un nuevo negocio con nombre, NIT o documento, correo, teléfono y datos del administrador[cite: 1]. | Alta[cite: 1] |
| **RF-02** | El sistema debe permitir iniciar y cerrar sesión con correo y contraseña[cite: 1]. | Alta[cite: 1] |
| **RF-03** | El sistema debe permitir recuperar la contraseña mediante un enlace enviado al correo[cite: 1]. | Alta[cite: 1] |
| **RF-04** | El administrador debe poder crear, editar, desactivar y eliminar usuarios de su negocio[cite: 1]. | Alta[cite: 1] |
| **RF-05** | El sistema debe manejar roles (Administrador y Vendedor) con permisos diferenciados por módulo[cite: 1]. | Alta[cite: 1] |
| **RF-06** | El sistema debe registrar un historial de acciones relevantes por usuario (quién vendió, modificó stock, anuló una venta)[cite: 1]. | Media[cite: 1] |

### 3.2 Gestión de inventario de licores

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-07** | El sistema debe permitir crear, consultar, editar y desactivar productos con: nombre, categoría (aguardiente, ron, whisky, cerveza, vino, otros), marca, presentación (volumen), código/SKU, precio de compra, precio de venta y stock[cite: 1]. | Alta[cite: 1] |
| **RF-08** | El sistema debe permitir buscar y filtrar productos por nombre, categoría, marca o código[cite: 1]. | Alta[cite: 1] |
| **RF-09** | El sistema debe descontar automáticamente del stock cada producto vendido[cite: 1]. | Alta[cite: 1] |
| **RF-10** | El sistema debe permitir registrar entradas de mercancía (compras a proveedores) que aumenten el stock[cite: 1]. | Alta[cite: 1] |
| **RF-11** | El sistema debe permitir ajustes manuales de inventario con motivo obligatorio (pérdida, rotura, conteo físico)[cite: 1]. | Alta[cite: 1] |
| **RF-12** | El sistema debe definir un stock mínimo por producto y alertar cuando se alcance o se supere hacia abajo[cite: 1]. | Alta[cite: 1] |
| **RF-13** | El sistema debe mostrar el historial de movimientos (kardex) de cada producto[cite: 1]. | Media[cite: 1] |
| **RF-14** | El sistema debe permitir gestionar proveedores (nombre, contacto, productos que surte)[cite: 1]. | Media[cite: 1] |
| **RF-15** | El sistema debe permitir importar el inventario inicial desde un archivo de Excel o CSV para facilitar la migración desde hojas de cálculo[cite: 1]. | Media[cite: 1] |
| **RF-16** | El sistema debe permitir registrar la fecha de vencimiento o lote en productos que lo requieran (cervezas, vinos u otros) y avisar de próximos vencimientos[cite: 1]. | Baja[cite: 1] |

### 3.3 Gestión de ventas y facturación

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-17** | El sistema debe permitir registrar una venta seleccionando productos y cantidades, con cálculo automático de subtotal, descuentos, impuestos y total[cite: 1]. | Alta[cite: 1] |
| **RF-18** | El sistema debe validar que haya stock suficiente antes de confirmar una venta y advertir al usuario en caso contrario[cite: 1]. | Alta[cite: 1] |
| **RF-19** | El sistema debe permitir registrar el método de pago (efectivo, transferencia, Nequi, Daviplata, tarjeta, mixto)[cite: 1]. | Alta[cite: 1] |
| **RF-20** | Para pagos en efectivo, el sistema debe calcular el valor a devolver (cambio)[cite: 1]. | Alta[cite: 1] |
| **RF-21** | El sistema debe generar un comprobante o factura de venta con numeración consecutiva, imprimible o descargable en PDF[cite: 1]. | Alta[cite: 1] |
| **RF-22** | El sistema debe permitir anular una venta (solo Administrador), restituyendo el stock y dejando registro del motivo[cite: 1]. | Alta[cite: 1] |
| **RF-23** | El sistema debe permitir apertura y cierre de caja por turno, con monto inicial y conteo final[cite: 1]. | Alta[cite: 1] |
| **RF-24** | El sistema debe realizar el cuadre de caja automático, mostrando el total esperado frente al valor contado y la diferencia[cite: 1]. | Alta[cite: 1] |
| **RF-25** | El sistema debe permitir registrar gastos y retiros de caja con descripción y monto[cite: 1]. | Media[cite: 1] |
| **RF-26** | El sistema debe permitir registrar clientes frecuentes y ventas fiadas (crédito) con control de saldos pendientes[cite: 1]. | Media[cite: 1] |
| **RF-27** | El sistema debe permitir consultar y buscar el historial de ventas por fecha, vendedor, método de pago o número de factura[cite: 1]. | Alta[cite: 1] |
| **RF-28** | El sistema debe permitir registrar ventas con lector de código de barras[cite: 1]. | Baja[cite: 1] |

### 3.4 Reportes y panel de control

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-29** | El sistema debe mostrar un panel de inicio con ventas del día, ganancia estimada, productos con bajo stock y últimos movimientos[cite: 1]. | Alta[cite: 1] |
| **RF-30** | El sistema debe generar reportes de ventas por día, semana, mes y rango personalizado[cite: 1]. | Alta[cite: 1] |
| **RF-31** | El sistema debe generar un reporte de ganancias (ingresos menos costo de los productos vendidos y gastos registrados)[cite: 1]. | Alta[cite: 1] |
| **RF-32** | El sistema debe generar un reporte de inventario valorizado y de productos con bajo stock[cite: 1]. | Alta[cite: 1] |
| **RF-33** | El sistema debe mostrar los productos más y menos vendidos[cite: 1]. | Media[cite: 1] |
| **RF-34** | El sistema debe permitir ver ventas por vendedor y por método de pago[cite: 1]. | Media[cite: 1] |
| **RF-35** | El sistema debe permitir exportar los reportes a PDF y Excel[cite: 1]. | Media[cite: 1] |
| **RF-36** | Los reportes deben actualizarse en tiempo real conforme se registren ventas y movimientos[cite: 1]. | Alta[cite: 1] |

### 3.5 Suscripción y pagos del servicio

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-37** | El sistema debe ofrecer planes de suscripción mensual y anual con sus características y precios visibles[cite: 1]. | Alta[cite: 1] |
| **RF-38** | El sistema debe permitir pagar la suscripción en línea mediante pasarela de pagos (PSE, tarjeta) y reportar pagos por transferencia digital (Nequi, Daviplata)[cite: 1]. | Alta[cite: 1] |
| **RF-39** | El sistema debe permitir un periodo de prueba o demo gratuita sin tarjeta de crédito[cite: 1]. | Alta[cite: 1] |
| **RF-40** | El sistema debe mostrar el estado de la suscripción (activa, por vencer, vencida) y notificar al administrador antes del vencimiento[cite: 1]. | Alta[cite: 1] |
| **RF-41** | El sistema debe restringir el acceso a las funciones de escritura cuando la suscripción esté vencida, conservando los datos del cliente y permitiendo su consulta o descarga[cite: 1]. | Media[cite: 1] |
| **RF-42** | El sistema debe permitir al equipo de soporte activar, suspender o prorrogar cuentas manualmente (recaudo directo)[cite: 1]. | Media[cite: 1] |
| **RF-43** | El sistema debe enviar recibos de pago de la suscripción por correo electrónico[cite: 1]. | Media[cite: 1] |

### 3.6 Soporte y ayuda

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-44** | El sistema debe incluir una sección de ayuda con guías breves y videos cortos de uso[cite: 1]. | Media[cite: 1] |
| **RF-45** | El sistema debe ofrecer un formulario o enlace directo (por ejemplo, WhatsApp) para solicitar soporte técnico[cite: 1]. | Media[cite: 1] |
| **RF-46** | El sistema debe incluir un recorrido guiado inicial para nuevos usuarios[cite: 1]. | Baja[cite: 1] |

### 3.7 Administración de la plataforma (equipo Licores Connect)

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-47** | El equipo de soporte debe poder consultar la lista de negocios suscritos, su plan y su estado[cite: 1]. | Media[cite: 1] |
| **RF-48** | El sistema debe permitir recibir sugerencias de los clientes para alimentar las actualizaciones continuas[cite: 1]. | Baja[cite: 1] |

---

## 4. Requisitos no funcionales

### 4.1 Usabilidad

| ID | Requisito |
| :--- | :--- |
| **RNF-01** | La interfaz debe ser intuitiva: un usuario sin conocimientos técnicos debe poder registrar su primera venta en menos de 5 minutos tras una breve inducción[cite: 1]. |
| **RNF-02** | El registro de una venta típica (hasta 5 productos) debe completarse en un máximo de 6 clics o toques[cite: 1]. |
| **RNF-03** | La interfaz debe ser responsiva y utilizable en celular, tableta y computador[cite: 1]. |
| **RNF-04** | El sistema debe estar en español de Colombia, con formatos de moneda (COP) y fecha locales[cite: 1]. |
| **RNF-05** | Los mensajes de error deben ser claros y orientar al usuario sobre cómo corregirlos[cite: 1]. |

### 4.2 Rendimiento

| ID | Requisito |
| :--- | :--- |
| **RNF-06** | Las pantallas principales deben cargar en menos de 3 segundos con conexión de 5 Mbps[cite: 1]. |
| **RNF-07** | El registro de una venta y la actualización del stock deben ejecutarse en menos de 2 segundos[cite: 1]. |
| **RNF-08** | Los reportes estándar deben generarse en menos de 5 segundos para hasta 50.000 registros[cite: 1]. |
| **RNF-09** | El sistema debe soportar al menos 100 negocios activos y 300 usuarios concurrentes en la versión 1.0[cite: 1]. |

### 4.3 Seguridad

| ID | Requisito |
| :--- | :--- |
| **RNF-10** | Todas las comunicaciones deben realizarse por HTTPS (TLS 1.2 o superior)[cite: 1]. |
| **RNF-11** | Las contraseñas deben almacenarse con hash seguro (bcrypt o Argon2); nunca en texto plano[cite: 1]. |
| **RNF-12** | Los datos de cada negocio deben estar aislados: ningún usuario puede ver información de otro negocio[cite: 1]. |
| **RNF-13** | El sistema debe aplicar control de acceso por rol en cada operación del servidor, no solo en la interfaz[cite: 1]. |
| **RNF-14** | El sistema no debe almacenar datos de tarjetas; el cobro se delega a la pasarela de pagos[cite: 1]. |
| **RNF-15** | La sesión debe expirar tras un periodo de inactividad configurable, y las cuentas deben bloquearse temporalmente tras varios intentos de acceso fallidos[cite: 1]. |
| **RNF-16** | El tratamiento de datos personales debe cumplir la Ley 1581 de 2012, incluyendo política de privacidad y autorización del titular[cite: 1]. |

### 4.4 Disponibilidad y confiabilidad

| ID | Requisito |
| :--- | :--- |
| **RNF-17** | El sistema debe tener una disponibilidad objetivo del 99 % mensual, excluyendo mantenimientos programados[cite: 1]. |
| **RNF-18** | Deben realizarse copias de seguridad automáticas diarias, con retención mínima de 30 días[cite: 1]. |
| **RNF-19** | Ante una falla, el sistema debe poder restaurarse a partir de la última copia en menos de 4 horas[cite: 1]. |
| **RNF-20** | Las operaciones de venta e inventario deben ser transaccionales: o se registran completas o no se registran, evitando descuadres de stock[cite: 1]. |

### 4.5 Mantenibilidad y escalabilidad

| ID | Requisito |
| :--- | :--- |
| **RNF-21** | El código debe estar organizado por módulos (ventas, inventario, reportes, usuarios, suscripción) y versionado en un repositorio Git[cite: 1]. |
| **RNF-22** | El sistema debe documentarse (API, base de datos y manual de usuario) para facilitar su mantenimiento[cite: 1]. |
| **RNF-23** | La arquitectura debe permitir aumentar la capacidad del hosting sin rediseñar la aplicación[cite: 1]. |
| **RNF-24** | Deben existir pruebas automatizadas para las reglas críticas (cálculo de totales, descuento de stock, cuadre de caja)[cite: 1]. |

### 4.6 Compatibilidad y portabilidad

| ID | Requisito |
| :--- | :--- |
| **RNF-25** | El sistema debe funcionar en las dos últimas versiones de Chrome, Edge, Firefox y Safari[cite: 1]. |
| **RNF-26** | El cliente no debe necesitar instalar software; basta un navegador y conexión a internet[cite: 1]. |
| **RNF-27** | Los clientes deben poder exportar sus datos (ventas, inventario) en formatos estándar (CSV/Excel)[cite: 1]. |

---

## 5. Requisitos de interfaces externas

### 5.1 Interfaces de usuario
* Diseño limpio, con botones grandes y flujos cortos pensados para el mostrador del negocio[cite: 1].
* Pantallas principales: inicio/panel, nueva venta, inventario, caja, reportes, usuarios, suscripción y ayuda[cite: 1].
* Uso de colores y alertas visuales para stock bajo y diferencias de caja[cite: 1].

### 5.2 Interfaces de hardware
* Compatibilidad opcional con impresoras de tickets (térmicas) mediante impresión desde el navegador[cite: 1].
* Compatibilidad opcional con lectores de código de barras que funcionen como teclado[cite: 1].

### 5.3 Interfaces de software

| Sistema externo | Propósito |
| :--- | :--- |
| **Pasarela de pagos (PSE, tarjetas)** | Cobro de suscripciones[cite: 1] |
| **Servicio de correo electrónico** | Notificaciones, recuperación de contraseña y recibos[cite: 1] |
| **Servicio de hosting en la nube** | Alojamiento de la aplicación y la base de datos[cite: 1] |
| **Nequi / Daviplata** | Recaudo por transferencia digital con confirmación manual o asistida[cite: 1] |

### 5.4 Interfaces de comunicación
* Protocolo HTTPS para toda la comunicación cliente-servidor[cite: 1].
* API interna tipo REST con intercambio de datos en formato JSON[cite: 1].

---

## 6. Criterios de aceptación y validación

| Criterio | Verificación |
| :--- | :--- |
| Un negocio puede registrarse, cargar productos y vender el mismo día[cite: 1] | Prueba funcional de extremo a extremo[cite: 1] |
| El stock se descuenta correctamente en el 100 % de las ventas de prueba[cite: 1] | Pruebas automatizadas y manuales[cite: 1] |
| El cuadre de caja coincide con el cálculo manual en las pruebas[cite: 1] | Comparación con casos reales del piloto[cite: 1] |
| Los reportes coinciden con los datos registrados[cite: 1] | Verificación cruzada con datos de ventas[cite: 1] |
| Un usuario sin experiencia técnica usa el sistema tras una inducción corta[cite: 1] | Pruebas de usabilidad con al menos 3 licorerías piloto[cite: 1] |
| Los pagos de suscripción se reflejan en el estado de la cuenta[cite: 1] | Pruebas en el entorno de pruebas de la pasarela[cite: 1] |
| Ningún negocio accede a datos de otro[cite: 1] | Pruebas de seguridad y de roles[cite: 1] |

La validación se realizará mediante pruebas piloto con negocios reales del sector, con ciclos de retroalimentación bajo metodología ágil[cite: 1].

---

## 7. Supuestos, restricciones y riesgos

### 7.1 Supuestos adicionales (por confirmar con el equipo)
* Se asume que las ventas se registran con impuestos básicos configurables (por ejemplo, IVA o impoconsumo) y que la facturación electrónica ante la DIAN queda para una versión posterior o mediante integración con un proveedor tecnológico[cite: 1].
* Se asume que los precios y planes definitivos se fijarán tras validar la disposición de pago con los negocios piloto[cite: 1].
* Las cifras de rendimiento y disponibilidad de la sección 4 son metas iniciales y deberán ajustarse a las capacidades del hosting contratado[cite: 1].

### 7.2 Riesgos

| Riesgo | Impacto | Mitigación |
| :--- | :--- | :--- |
| Poca experiencia del equipo en pagos y seguridad[cite: 1] | Alto[cite: 1] | Delegar el cobro a la pasarela; revisiones de código entre pares[cite: 1] |
| Resistencia de los tenderos a dejar libretas y Excel[cite: 1] | Medio[cite: 1] | Demos gratuitas, importación desde Excel y soporte cercano[cite: 1] |
| Conexión a internet inestable en negocios pequeños[cite: 1] | Medio[cite: 1] | Interfaz ligera; evaluar modo sin conexión en versiones futuras[cite: 1] |
| Tiempo limitado del equipo (5 estudiantes)[cite: 1] | Alto[cite: 1] | Priorizar requisitos de prioridad Alta y entregar en ciclos cortos[cite: 1] |
| Cambios normativos sobre venta de licores o facturación[cite: 1] | Medio[cite: 1] | Diseño modular y revisión periódica de la normativa[cite: 1] |
| Pérdida de datos[cite: 1] | Alto[cite: 1] | Copias de seguridad diarias y pruebas de restauración[cite: 1] |

### 7.3 Posibles mejoras futuras
* Facturación electrónica integrada con la DIAN[cite: 1].
* Modo sin conexión con sincronización posterior[cite: 1].
* Aplicación móvil nativa[cite: 1].
* Alertas de reposición y sugerencias de pedido a proveedores[cite: 1].
* Módulo de domicilios y catálogo en línea[cite: 1].

---

## 8. Matriz de trazabilidad (resumen)

| Necesidad del proyecto | Requisitos relacionados |
| :--- | :--- |
| Registro rápido de ventas[cite: 1] | RF-17 a RF-21, RNF-01, RNF-02, RNF-07[cite: 1] |
| Control automático de stock[cite: 1] | RF-07 a RF-12, RNF-20[cite: 1] |
| Reducción de errores en facturación y cuadre de caja[cite: 1] | RF-21 a RF-24, RNF-20, RNF-24[cite: 1] |
| Reportes financieros en tiempo real[cite: 1] | RF-29 a RF-36, RNF-08[cite: 1] |
| Fácil de usar, sin conocimientos técnicos[cite: 1] | RF-44 a RF-46, RNF-01 a RNF-05[cite: 1] |
| Bajo costo y accesible desde cualquier dispositivo[cite: 1] | RF-37 a RF-39, RNF-03, RNF-23, RNF-26[cite: 1] |
| Suscripción SaaS y medios de pago[cite: 1] | RF-37 a RF-43, RNF-14[cite: 1] |
| Soporte cercano y actualizaciones continuas[cite: 1] | RF-42, RF-44, RF-45, RF-47, RF-48[cite: 1] |