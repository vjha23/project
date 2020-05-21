import java.util.Scanner;

public class CoffeeMachine {
	static int cost=550;
	static int water=400;
	static int milk=540;
	static int beans=120;
	static int cups=9;
	public static void printResults(int water,int milk,int beans,int cups,int money) {
		   System.out.println("The coffee machine has:");
	        System.out.println(water + " of water");
	        System.out.println(milk + " of milk");
	        System.out.println(beans + " of coffee beans");
	        System.out.println(cups + " of disposable cups");
	        System.out.println(money + " of money");
	}
	
	public static boolean isEnoughIngredients(int needWater,int needMilk,int needBeans) {
		int needCups=1;
		boolean isEnoughIngredients=true;
		if(water<needWater) {
			System.out.println("Sorry,Not enough water");
			isEnoughIngredients=false;
		}
		if(milk<needMilk) {
			System.out.println("Sorry,Not enough milk");
			isEnoughIngredients=false;
		}
		if(beans<needBeans) {
			System.out.println("Sorry,Not enough beans");
			isEnoughIngredients=false;
		}
		if(cups<needCups) {
			System.out.println("Sorry,Not enough disposable cups");
			isEnoughIngredients=false;
		}
		return isEnoughIngredients;
	}
	public static void buy(Scanner in) {
		System.out.println("What do you want to buy?1-espresso,2-latte,3-cappucino,back-to main menu");
		String type=in.next();
		switch(type) {
		case "1":if(isEnoughIngredients(250,0,16)) {
				 water-=250;
				 beans -= 16;
				 cups--;
				 cost += 4;
				}
				 break;
		case "2":if(isEnoughIngredients(250,0,16)) {
				 water -= 350;
				 milk -= 75;
				 beans -= 20;
				 cups--;
				 cost+= 7;
		}
				 break;
		case "3":if(isEnoughIngredients(250,0,16)) {
				 water -= 200;
				 milk -= 100;
				 beans -= 12;
				 cups--;
				 cost += 6;
		}
				 break;
		case "back":break;
		default:break;
		}
	}
	public static void fill(Scanner in) {
		System.out.println("Enter How many ml of water you want to fill");
		water+=in.nextInt();
		System.out.println("Enter How many ml of milk you want to add");
		milk+=in.nextInt();
		System.out.println("Enter how many grams of coffee beans you want to add");
		beans+=in.nextInt();
		System.out.println("Enter How many disposal cups you want to add");
		cups+=in.nextInt();
	}
	public static void take(Scanner in) {
		System.out.println("I gave you $"+cost);
		cost=0;
	}
	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		boolean enable=true;
		while(enable) {
			System.out.println("Write action(buy,fill,take,remaining,exit):");
			String action=in.nextLine();
			switch(action) {
			case "buy":buy(in);
					   break;
			case "fill":fill(in);
						break;
			case "take":take(in);
						break;
			case "remaining":printResults(water,milk,beans,cups,cost);
								break;
			case "exit":enable=false;
						break;
			default:break;
						
			}
		}
	}
}
