/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.mascotas;

/**
 *
 * @author macbookair
 */
public class Mascotas {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        
        Perro[] perros = new Perro[3];
        
        
        perros[0]= new Perro();
        perros[0].nombre ="firulais";
        
        perros[1]= new Perro();
        perros[1].nombre ="rufus";
        
        perros[2]= new Perro();
        perros[2].nombre ="MAX";
        
        for (Perro perro : perros){
        
            System.out.println(perro.nombre);
            perro.comer();
            perro.ladrar();
            System.out.println();
            
        }
        
        
        
    }
}
