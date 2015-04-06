import java.io.*;
import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
class re implements ActionListener
{
  JFrame fr,fr2;
  JButton b1,b2,b3;
  re()
  {
     fr=new JFrame("start the minor project ");
     fr.setLayout(new GridLayout(1,2));
     b1=new JButton("start");
     b2=new JButton("ENCODE");
     b3=new JButton("DECODE");
     b1.addActionListener(this);
     fr.add(b1);
     fr.setSize(400,400);
     fr.setVisible(true);
     b2.addActionListener(this);
     b3.addActionListener(this);


  }
  public void actionPerformed(ActionEvent e)
  {
    if(e.getSource()==b1)
    {
      fr2.setLayout(new GridLayout(2,1));
      fr2=new JFrame("Activity starts");
      fr2.add(b2);
      fr2.add(b3);
      fr2.setSize(300,300);
      fr2.setVisible(true);
      fr.setVisible(false);


    }

  }
  public static void main(String args[])throws IOException
  {
    new re();


  }

}
