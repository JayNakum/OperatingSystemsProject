package com.example.cpuscheduling

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.viewpager.widget.PagerAdapter
import kotlinx.android.synthetic.main.card_item.view.*

class Adapter(private val context: Context, private val myModelArrayList: ArrayList<Model>) :PagerAdapter(){
    override fun isViewFromObject(view: View, `object`: Any): Boolean {
        return view == `object`
    }

    override fun getCount(): Int {

        return myModelArrayList.size
    }

    override fun instantiateItem(container: ViewGroup, position: Int): Any {
        val view = LayoutInflater.from(context).inflate(R.layout.card_item, container,false)

        val model =myModelArrayList[position]
        val title = model.title
        val description = model.description
        val image = model.image

        view.bannerTv.setImageResource(image)
        view.titleTv.text = title
        view.description.text = description

        view.setOnClickListener{
            Toast.makeText(context, "$title \n $description",Toast.LENGTH_SHORT).show()
        }

        container.addView(view,position)
        return view
    }

    override fun destroyItem(container: ViewGroup, position: Int, `object`: Any) {
        container.removeView(`object` as View)
    }
}