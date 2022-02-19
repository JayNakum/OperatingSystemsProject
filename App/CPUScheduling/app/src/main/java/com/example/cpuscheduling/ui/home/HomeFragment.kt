package com.example.cpuscheduling.ui.home

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.appcompat.app.ActionBar
import androidx.fragment.app.Fragment
import androidx.viewpager.widget.ViewPager
import com.example.cpuscheduling.R
import com.example.cpuscheduling.databinding.FragmentHomeBinding

class HomeFragment : Fragment() {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    private lateinit var actionBar: ActionBar
    private lateinit var myModelList: ArrayList<Model>
    private lateinit var Adapter:com.example.cpuscheduling.ui.home.Adapter

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {

        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        val root: View = binding.root

        return root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        loadCards()
        binding.viewPager.addOnPageChangeListener(object: ViewPager.OnPageChangeListener{

            override fun onPageScrolled(
                position: Int,
                positionOffset: Float,
                positionOffsetPixels: Int
            ) {
//                val title = myModelList[position].title
//                actionBar.title = title
            }

            override fun onPageSelected(position: Int) {

            }

            override fun onPageScrollStateChanged(state: Int) {

            }
        })
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    private fun loadCards() {
        myModelList = ArrayList()

        myModelList.add(
            Model("CPU Scheduling ",
            "CPU Scheduling is a process of determining which process will own CPU for execution while another process is on hold",
            R.drawable.ic_cpu))

        myModelList.add(
            Model("Preemptive ",
            "Preemptive Scheduling is a CPU scheduling technique that works by dividing time slots of CPU to a given process.",
            R.drawable.ic_verify)
        )

        myModelList.add(
            Model("Non-Preemptive ",
            "Non-preemptive Scheduling is a CPU scheduling technique the process takes the resource (CPU time) and holds it till the process gets terminated or is pushed to the waiting state.",
            R.drawable.ic_verify)
        )



        Adapter = com.example.cpuscheduling.ui.home.Adapter(requireContext(), myModelList)

        binding.viewPager.adapter = Adapter

        binding.viewPager.setPadding(10,0,10,0)


    }


}