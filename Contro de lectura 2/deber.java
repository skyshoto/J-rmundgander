import java.util.ArrayList;
import java.util.List;

// Clase Vehículo
class Vehiculo {
    public String modelo;
    public String matricula;

    public Vehiculo(String modelo, String matricula) {
        this.modelo = modelo;
        this.matricula = matricula;
    }

    public void alquilar() {
        System.out.println("El vehículo con matrícula " + matricula + " ha sido alquilado.");
    }

    public void devolver() {
        System.out.println("El vehículo con matrícula " + matricula + " ha sido devuelto.");
    }
}

// Clase Cliente
class Cliente {
    public String nombre;
    public String telefono;

    public Cliente(String nombre, String telefono) {
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public void alquilarVehiculo() {
        System.out.println("El cliente " + nombre + " ha alquilado un vehículo.");
    }

    public void devolverVehiculo() {
        System.out.println("El cliente " + nombre + " ha devuelto un vehículo.");
    }
}

// Clase Agencia
class Agencia {
    public String nombre;
    public String direccion;
    private List<Vehiculo> vehiculos;

    public Agencia(String nombre, String direccion) {
        this.nombre = nombre;
        this.direccion = direccion;
        this.vehiculos = new ArrayList<>();
    }

    public void agregarVehiculo(Vehiculo vehiculo) {
        vehiculos.add(vehiculo);
        System.out.println("Vehículo " + vehiculo.modelo + " agregado a la agencia.");
    }

    public void listarVehiculos() {
        System.out.println("Vehículos disponibles en la agencia " + nombre + ":");
        for (Vehiculo vehiculo : vehiculos) {
            System.out.println("- Modelo: " + vehiculo.modelo + ", Matrícula: " + vehiculo.matricula);
        }
    }
}

// Clase Empleado
class Empleado {
    public Cliente cliente;
    public Vehiculo vehiculo;

    public Empleado(Cliente cliente, Vehiculo vehiculo) {
        this.cliente = cliente;
        this.vehiculo = vehiculo;
    }

    public void registrar() {
        System.out.println("El cliente " + cliente.nombre + " ha registrado el alquiler del vehículo " + vehiculo.modelo + ".");
    }

    public void cancelar() {
        System.out.println("El cliente " + cliente.nombre + " ha cancelado el alquiler del vehículo " + vehiculo.modelo + ".");
    }
}

// Clase principal
public class deber {
    public static void main(String[] args) {
        // Crear objetos
        Vehiculo vehiculo1 = new Vehiculo("Toyota Corolla", "ABC-123");
        Vehiculo vehiculo2 = new Vehiculo("Honda Civic", "XYZ-456");
        Cliente cliente1 = new Cliente("María López", "555-1234");
        Agencia agencia = new Agencia("Agencia Central", "Calle Principal 123");

        // Operaciones
        agencia.agregarVehiculo(vehiculo1);
        agencia.agregarVehiculo(vehiculo2);

        agencia.listarVehiculos();

        cliente1.alquilarVehiculo(); // Alquilar vehículo
        cliente1.devolverVehiculo(); // Devolver vehículo

        Empleado empleado1 = new Empleado(cliente1, vehiculo1);
        empleado1.registrar(); // Registrar alquiler
        empleado1.cancelar(); // Cancelar alquiler
    }
}
