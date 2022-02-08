package com.example.cpuscheduling

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.appcompat.app.ActionBar
import androidx.viewpager.widget.ViewPager
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    private lateinit var actionBar:ActionBar;
    private lateinit var myModelList: ArrayList<Model>
    private lateinit var Adapter:Adapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        actionBar = this.supportActionBar!!

        loadCards()
        viewPager.addOnPageChangeListener(object: ViewPager.OnPageChangeListener{

            override fun onPageScrolled(
                position: Int,
                positionOffset: Float,
                positionOffsetPixels: Int
            ) {
                val title = myModelList[position].title
                actionBar.title = title
            }

            override fun onPageSelected(position: Int) {

            }

            override fun onPageScrollStateChanged(state: Int) {

            }
        })
    }

    private fun loadCards() {
        myModelList = ArrayList()

        myModelList.add(Model("CPU Scheduling ",
            "CPU Scheduling is a process of determining which process will own CPU for execution while another process is on hold",
            R.drawable.ic_cpu))

        myModelList.add(Model("Preemptive ",
            "Preemptive Scheduling is a CPU scheduling technique that works by dividing time slots of CPU to a given process.",
        R.drawable.ic_verify))

        myModelList.add(Model("Non-Preemptive ",
            "Non-preemptive Scheduling is a CPU scheduling technique the process takes the resource (CPU time) and holds it till the process gets terminated or is pushed to the waiting state.",
        R.drawable.ic_verify))

        Adapter = Adapter(this, myModelList)


        viewPager.adapter = Adapter

        viewPager.setPadding(10,0,10,0)


    }

}